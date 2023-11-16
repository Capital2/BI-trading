import requests as req
from pathlib import Path
import pandas as pd


class Extract:
    def __init__(self, url: str, headers: dict, params: dict):        
        self.url = url
        self.headers = headers
        self.params = params
        self.filename = None
        
    def get_file_args(self):
        return [self.params["startdate"].replace("/", "-").replace(" ", "T").replace(":", "-"), self.params["enddate"].replace("/", "-").replace(" ", "T").replace(":", "-")  ]

    def download_share_data(self, share: str = None):     
        startdate, enddate = self.get_file_args()
        if share != None:
            tmp_file_name = f"{share}_{startdate}_{enddate}.csv"
        else:
            tmp_file_name = f"share_{startdate}_{enddate}.csv"
        self.filename = tmp_file_name
            
        tmp_destination = Path(Path.cwd(), "tmp", self.filename)
        res = req.get(self.url, headers=self.headers, params=self.params)
        if res.status_code == 200:    
            with open(tmp_destination, "wb") as file:
                file.write(res.content)                
        else:
            print("Failed to download data. Status code:", res.status_code)

    def read_share_data(self) -> pd.DataFrame:        
        source = Path(Path.cwd(), "tmp", self.filename)
        df = pd.read_csv(source)
        return df
