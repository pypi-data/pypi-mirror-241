import numpy as np
import pandas as pd
import os
from datetime import timedelta, datetime, time
from volstreet.config import logger
from volstreet.vectorized_blackscholes import add_greeks_to_dataframe
from volstreet.backtests.underlying_info import UnderlyingInfo
from volstreet.backtests.framework import IntradayBacktest
from volstreet.parallelization import execute_in_parallel
from volstreet.utils.data_io import make_directory_if_needed


class DeltaBackTest(IntradayBacktest):
    RESULTS_FOLDER = "data\\delta_backtests\\"

    def __init__(self, underlying: UnderlyingInfo):
        super().__init__(underlying)

    def get_strike_columns(self):
        return ["call_strike", "put_strike"]

    def merge_with_option_prices(
        self,
        date_frame_to_merge: pd.DataFrame,
    ) -> pd.DataFrame:
        option_prices = self.option_prices.reset_index()

        merged_with_call_prices = date_frame_to_merge.merge(
            option_prices[["timestamp", "expiry", "call_price", "strike"]],
            left_on=["timestamp", "expiry", "call_strike"],
            right_on=["timestamp", "expiry", "strike"],
        )
        merged_with_put_prices = merged_with_call_prices.merge(
            option_prices[["timestamp", "expiry", "put_price", "strike"]],
            left_on=["timestamp", "expiry", "put_strike"],
            right_on=["timestamp", "expiry", "strike"],
        )
        merged_with_put_prices.drop(columns=["strike_x", "strike_y"], inplace=True)

        return merged_with_put_prices

    def select_equal_strikes(
        self,
        snapshot: pd.DataFrame,
    ) -> tuple[int, int]:
        with_option_prices = self.merge_with_option_prices(
            snapshot,
        )
        equal_strike_index = (
            ((with_option_prices.call_price - with_option_prices.put_price).abs())
            / np.minimum(with_option_prices.call_price, with_option_prices.put_price)
        ).argmin()
        equal_strike = with_option_prices.iloc[equal_strike_index]

        return equal_strike.call_strike, equal_strike.put_strike

    def prepare_segment_for_processing(
        self,
        segment_prices: pd.DataFrame,
    ):
        """Prepares the segment for processing by adding the call and put strikes and
        merging with option prices and adding greeks"""

        entry_snapshot = self.snapshot_at_entry(segment_prices.iloc[0])
        potential_strikes = np.unique(
            entry_snapshot[["call_strike", "put_strike"]].values
        ).tolist()
        if not all(self.strike_available(potential_strikes)):
            logger.info(
                f"Fetching missed strikes {potential_strikes} and some additional strikes for {segment_prices.iloc[0].name}"
            )
            additional_strikes = np.arange(
                min(potential_strikes) - 10 * self.underlying.base,
                max(potential_strikes)
                + 10 * self.underlying.base
                + self.underlying.base,
                self.underlying.base,
            ).tolist()
            self.fetch_missed_strikes(additional_strikes, segment_prices.iloc[0].name)
        self.check_option_prices_availability(entry_snapshot)
        call_strike, put_strike = self.select_equal_strikes(entry_snapshot)
        segment_prices["call_strike"] = call_strike
        segment_prices["put_strike"] = put_strike
        self.check_option_prices_availability(segment_prices)
        segment_prices_with_option_prices = self.merge_with_option_prices(
            segment_prices
        )
        segment_prices_with_option_prices = add_greeks_to_dataframe(
            segment_prices_with_option_prices
        )
        segment_prices_with_option_prices.set_index("timestamp", inplace=True)
        return segment_prices_with_option_prices

    @staticmethod
    def process_result(
        segment: pd.DataFrame, segment_result: pd.DataFrame
    ) -> pd.DataFrame:
        columns = segment_result.columns.tolist()
        additional_cols = [
            "open",
            "call_strike",
            "put_strike",
            "call_price",
            "put_price",
            "call_ivs",
            "put_ivs",
            "call_deltas",
            "put_deltas",
            "call_gammas",
            "put_gammas",
        ]
        processed_result = segment_result.merge(
            segment[additional_cols], left_index=True, right_index=True
        )
        processed_result = processed_result[additional_cols + columns]
        return processed_result

    def reset_state(self):
        self.expiry = None
        self._option_prices = pd.DataFrame()
        self.unique_strikes = []
        return self

    def prepare_index_prices(self, from_date, to_date, only_expiry):
        index_prices = self.fetch_index_prices(self.underlying.name, from_date, to_date)
        index_prices.set_index("timestamp", inplace=True)
        if only_expiry:
            index_prices = index_prices[
                [
                    _date in self.underlying.expiry_dates.date
                    for _date in index_prices.index.date
                ]
            ]
        return index_prices

    def run_day(
        self,
        intraday_prices: pd.DataFrame,
        start_after: tuple[int, int] = (9, 15),
        scan_exit_time: tuple[int, int] = (14, 40),
    ) -> pd.DataFrame:
        intraday_prices = intraday_prices[
            (intraday_prices.index.time > time(*start_after))
        ].copy()

        if intraday_prices.index[-1].time() < time(*scan_exit_time):
            logger.info(
                f"Delta backtest: Skipping {intraday_prices.index[-1].date} as the last timestamp is before scan exit time"
            )
            return pd.DataFrame()

        expiry = self.determine_expiry(intraday_prices.iloc[0])
        if self.expiry is None or self.expiry != expiry:
            self.reset_state()
            self.expiry = expiry
            self.fetch_and_store_option_prices(
                intraday_prices.iloc[0], 10
            )  # Fetching 10 strikes each side
        intraday_prices["expiry"] = self.expiry.strftime("%d%b%y").upper()
        intraday_prices["time_to_expiry"] = (
            self.expiry - intraday_prices.index
        ).total_seconds() / (60 * 60 * 24 * 365)
        current_segment = intraday_prices.copy()
        segment_results = []
        while not current_segment.empty and current_segment.index[0].time() < time(
            *scan_exit_time
        ):
            current_segment = self.prepare_segment_for_processing(current_segment)
            segment_result = process_segment(
                current_segment, 1000, 1, 4000
            )  # Hard-coding the values for now
            segment_result = self.process_result(current_segment, segment_result)
            segment_results.append(segment_result)
            current_segment = intraday_prices[
                intraday_prices.index >= segment_result.index[-1]
            ].copy()
        return pd.concat(segment_results)

    def make_result_folder(self, folder_name: str = None):
        # Deciding the folder to store the results in
        directory = os.path.join(DeltaBackTest.RESULTS_FOLDER, self.underlying.name)
        if folder_name is None:
            if os.path.exists(directory):
                folder_number = len(os.listdir(directory)) + 1
            else:
                folder_number = 1
            folder_name = f"backtest_{folder_number}\\"
        else:
            folder_name = f"{folder_name}\\"
        directory = os.path.join(directory, folder_name)
        make_directory_if_needed(directory)
        return directory

    def run_backtest_subset(
        self,
        underlying: UnderlyingInfo,
        index_prices: pd.DataFrame,
        date_subset: list[datetime],
        start_after: tuple[int, int],
        scan_exit_time: tuple[int, int],
        result_folder: str,
    ) -> None:
        """
        Runs the backtest for a subset of dates.
        """

        self.underlying = underlying
        self.expiry = None
        self._option_prices = pd.DataFrame()
        self.unique_strikes = []

        logger.info(f"Running backtest for {date_subset}")

        for date in date_subset:
            try:
                # Filter prices for the specific date
                prices = index_prices[index_prices.index.date == date]
                result = self.run_day(prices, start_after, scan_exit_time)
                if not result.empty:
                    backtest_date = result.index[0].date()
                    filename = os.path.join(result_folder, f"{backtest_date}.csv")
                    result.to_csv(filename)
            except Exception as e:
                logger.error(f"Error while running backtest for {date}: {e}")

    def run_backtest_in_parallel(
        self,
        from_date: str | datetime,
        to_date: str | datetime = None,
        only_expiry: bool = False,
        start_after: tuple[int, int] = (9, 15),
        scan_exit_time: tuple[int, int] = (14, 40),
        folder_name: str = None,
        n_jobs: int = 5,
    ):
        """
        Runs the backtest in parallel by splitting the index prices based on unique dates.
        """
        index_prices = self.prepare_index_prices(from_date, to_date, only_expiry)
        result_folder = self.make_result_folder(folder_name)

        # Split the unique dates into chunks for parallel processing
        split_dates = np.array_split(np.unique(index_prices.index.date), 5)

        # Prepare tasks for parallel execution
        tasks = [
            (
                self.run_backtest_subset,
                (
                    self.underlying,
                    index_prices[
                        pd.DatetimeIndex(index_prices.index.date).isin(date_chunk)
                    ],
                    date_chunk.tolist(),
                    start_after,
                    scan_exit_time,
                    result_folder,
                ),
            )
            for date_chunk in split_dates
        ]
        logger.info(f"Prepared the following tasks: {tasks}. Running in parallel...")
        # Execute tasks in parallel
        results = execute_in_parallel(tasks, n_jobs=n_jobs)

        return results

    def run_backtest(
        self,
        from_date: str | datetime,
        to_date: str | datetime = None,
        only_expiry: bool = False,
        start_after: tuple[int, int] = (9, 15),
        scan_exit_time: tuple[int, int] = (14, 40),
        folder_name: str = None,
    ):
        index_prices = self.prepare_index_prices(from_date, to_date, only_expiry)
        result_folder = self.make_result_folder(folder_name)
        for date, prices in index_prices.groupby(index_prices.index.date):
            try:
                result = self.run_day(prices, start_after, scan_exit_time)
                if not result.empty:
                    backtest_date = result.index[0].date()
                    filename = os.path.join(result_folder, f"{backtest_date}.csv")
                    result.to_csv(filename)
            except Exception as e:
                logger.error(f"Error while running backtest for {date}: {e}")
                continue

    def consolidate_backtest(self, folder_name):
        path = os.path.join(
            DeltaBackTest.RESULTS_FOLDER, self.underlying.name, folder_name
        )
        full_df = pd.DataFrame()
        for day in os.listdir(path):
            day_df = pd.read_csv(os.path.join(path, day))
            full_df = pd.concat([full_df, day_df], ignore_index=True)
        full_df.set_index("timestamp", inplace=True)
        full_df.index = pd.to_datetime(full_df.index, dayfirst=True, format="mixed")
        return full_df


def update_positions_and_premium(
    row: pd.Series,
    net_delta: float,
    call_positions: int,
    put_positions: int,
    premium_received: float,
    delta_threshold: float,
) -> tuple[int, int, float]:
    if (
        net_delta > delta_threshold
    ):  # Net delta is positive, sell the required call amount to neutralize
        qty_call_to_sell = int((abs(net_delta) - 0) / row["call_deltas"])
        call_positions -= qty_call_to_sell
        premium_received += qty_call_to_sell * row["call_price"]
    elif (
        net_delta < -delta_threshold
    ):  # Net delta is negative, sell another put to neutralize
        qty_put_to_sell = int((abs(net_delta) - 0) / abs(row["put_deltas"]))
        put_positions -= qty_put_to_sell
        premium_received += qty_put_to_sell * row["put_price"]

    return call_positions, put_positions, premium_received


def process_segment(
    prepared_segment: pd.DataFrame,
    qty_to_trade: int,
    delta_interval_minutes: int,
    exit_qty: int,
) -> pd.DataFrame:
    entry_data = prepared_segment.iloc[0]
    call_positions = -qty_to_trade  # Sell call
    put_positions = -qty_to_trade  # Sell put
    premium_received = (
        entry_data["call_price"] * qty_to_trade + entry_data["put_price"] * qty_to_trade
    )  # Update PnL
    delta_check_interval = entry_data.name + timedelta(minutes=delta_interval_minutes)

    # Lists to store PnL and net delta for each minute
    premium_received_history = []
    net_delta_history = []
    call_position_history = []
    put_position_history = []
    mtm_history = []

    # Iterate through the data minute by minute
    for i, row in prepared_segment.iterrows():
        net_delta = (
            call_positions * row["call_deltas"] + put_positions * row["put_deltas"]
        )

        # Calculation of delta threshold
        one_min_std = 0.00035 * row["open"]
        position_gamma = row["call_gammas"] * abs(call_positions) + row[
            "put_gammas"
        ] * abs(put_positions)
        delta_threshold = one_min_std * position_gamma

        if abs(net_delta) > delta_threshold and i >= delta_check_interval:
            (
                call_positions,
                put_positions,
                premium_received,
            ) = update_positions_and_premium(
                row,
                net_delta,
                call_positions,
                put_positions,
                premium_received,
                delta_threshold,
            )

            # Update the net delta
            net_delta = (
                call_positions * row["call_deltas"] + put_positions * row["put_deltas"]
            )
            delta_check_interval = i + timedelta(minutes=delta_interval_minutes)

            if abs(call_positions) > exit_qty or abs(put_positions) > exit_qty:
                # Exit if max position size is reached
                # Make the final appends before breaking
                premium_received_history.append(premium_received)
                net_delta_history.append(net_delta)
                call_position_history.append(call_positions)
                put_position_history.append(put_positions)
                mtm_history.append(
                    call_positions * row["call_price"]
                    + put_positions * row["put_price"]
                )
                break

        # Append histories
        premium_received_history.append(premium_received)
        net_delta_history.append(net_delta)
        call_position_history.append(call_positions)
        put_position_history.append(put_positions)
        mtm_history.append(
            call_positions * row["call_price"] + put_positions * row["put_price"]
        )

    segment_result = pd.DataFrame(
        {
            "call_positions": call_position_history,
            "put_positions": put_position_history,
            "net_delta": net_delta_history,
            "premium": premium_received_history,
            "mtm": mtm_history,
        },
        index=prepared_segment[(prepared_segment.index <= i)].index,
    )

    return segment_result


def summarize_results(df: pd.DataFrame) -> pd.DataFrame:
    # Identify duplicate timestamps, which signify exit points
    duplicate_times = df[df.index.duplicated(keep="last")]

    # Finding the last row of each day
    final_exits = df.loc[
        df.groupby(df.index.date).apply(lambda x: x.iloc[-1].name).tolist()
    ]

    exit_times = pd.concat([duplicate_times, final_exits])

    # For each duplicate date, sum the 'premium' and 'mtm' to calculate profit
    exit_times["profit"] = exit_times["premium"] + exit_times["mtm"]

    return exit_times.sort_index()


def extreme_summary(summary: pd.DataFrame) -> pd.DataFrame:
    summary = summary.copy()
    exposure_in_shares = abs(
        np.minimum(summary.call_positions, summary.put_positions).median()
    )  # Taking the median of the higher of the two positions. Median to avoid outliers from depressing the percentage return.
    summary["exposure"] = exposure_in_shares * summary.open
    summary["profit_percentage"] = (summary.profit / summary.exposure) * 100
    return summary.groupby(summary.index.date).profit_percentage.sum()
