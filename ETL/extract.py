import requests as req
from pathlib import Path
import pandas as pd


class Extract:
    def __init__(self, startdate: str, enddate: str):
        # example of the startdate: "11/10/2022 00:00:00"
        # example of the enddate: "11/10/2023 00:00:00"

        self.url = "https://www.marketwatch.com/investing/stock/gme/downloaddatapartial"
        self.headers = None
        self.params = {
            "startdate": startdate,
            "enddate": enddate,
            "daterange": "d30",
            "frequency": "p1d",
            "csvdownload": "true",
            "downloadpartial": "false",
            "newdates": "false",
        }
        
    def get_file_args(self):
        return [self.params["startdate"].replace("/", "-").replace(" ", "T").replace(":", "-"), self.params["enddate"].replace("/", "-").replace(" ", "T").replace(":", "-")  ]

    def download_gme_data(self):     
        startdate, enddate = self.get_file_args()
        tmp_destination = Path(Path.cwd(), "tmp", f"gme_data_{startdate}_{enddate}.csv")
        res = req.get(self.url, headers=self.headers, params=self.params)
        if res.status_code == 200:    
            with open(tmp_destination, "wb") as file:
                file.write(res.content)                
        else:
            print("Failed to download data. Status code:", res.status_code)

    def read_gme_data(self) -> pd.DataFrame:
        startdate, enddate = self.get_file_args()
        source = Path(Path.cwd(), "tmp", f"gme_data_{startdate}_{enddate}.csv")
        df = pd.read_csv(source)
        return df
