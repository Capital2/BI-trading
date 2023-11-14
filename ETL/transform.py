import pandas as pd
from finta import TA


class Transform:
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data
        self.psma = 12  # Periods for simple moving average

    def cast(self):
        # Cast the pandas dataframe columns to the correct types
        self.data["Date"] = pd.to_datetime(self.data["Date"])
        self.data["Volume"] = self.data["Volume"].apply(
            lambda x: float(x.replace(",", ""))
        )

    def validate(self):
        # Correct any any anomalies in the data
        self.data.fillna(0, inplace=True)

    def correct_index(self):
        # Setting the Date column as index (gym_anytrading requirement)
        # self.data.set_index('Date', inplace=True)
        self.data.reset_index(drop=True, inplace=True)

    def sort(self):
        # Add df.sort_index() so the data isn't reversed. The model is training and predicting on reversed data. Gym-anytrading does not automatically sort by the date index.
        # self.data.sort_index(ascending=True, inplace=True)
        self.data.sort_values(by="Date", inplace=True)

    def calculate_indicators(self):
        # Calculating the financial indicators
        self.data["SMA"] = TA.SMA(self.data, self.psma)
        self.data["RSI"] = TA.RSI(self.data)
        self.data["OBV"] = TA.OBV(self.data)

    def correct_column_names(self):
        self.data.rename(
            columns={
                "Date": "date",
                "Open": "open",
                "High": "high",
                "Low": "low",
                "Close": "close",
                "Volume": "volume",
            },
            inplace=True,
        )

    def perform_data_transformations(self):
        # Perform all the data transformations       
        self.cast()
        self.sort()
        self.calculate_indicators()
        self.validate()
        self.correct_column_names()
        self.correct_index()        
