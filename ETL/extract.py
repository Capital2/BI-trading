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

    def download_gme_data(self):        
        tmp_destination = Path(Path.cwd(), "tmp", f"gme_data_{self.params['startdate']}_{self.params['enddate']}.csv")
        res = req.get(self.url, headers=self.headers, params=self.params)
        if res.status_code == 200:    
            with open(tmp_destination, "wb") as file:
                file.write(res.content)                
        else:
            print("Failed to download data. Status code:", res.status_code)

    def read_gme_data(self) -> pd.DataFrame:
        source = Path(Path.cwd(), "tmp", f"gme_data_{self.params['startdate']}_{self.params['enddate']}.csv")
        df = pd.read_csv(source)
        return df
