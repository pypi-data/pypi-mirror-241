import pandas as pd
from datetime import datetime
import pickle


class UnderlyingInfo:
    def __init__(self, name):
        self.name = name.upper()
        self.base = self._get_base()
        self.expiry_dates = self._get_expiry_dates()

    def _get_base(self):
        if self.name in ["NIFTY", "FINNIFTY"]:
            return 50
        elif self.name == "BANKNIFTY":
            return 100
        elif self.name == "MIDCPNIFTY":
            return 25
        else:
            raise ValueError("Invalid index name")

    def _get_expiry_dates(self):
        with open("volstreet\\historical_info\\index_expiries.pkl", "rb") as file:
            all_expiry_dates = pickle.load(file)
            index_expiry_dates = all_expiry_dates[self.name.upper()]
            index_expiry_dates = [
                *map(
                    lambda x: datetime.strptime(x, "%d%b%y").replace(
                        hour=15, minute=30
                    ),
                    index_expiry_dates,
                )
            ]
            return pd.DatetimeIndex(sorted(index_expiry_dates))
