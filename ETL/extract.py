import requests as req
from pathlib import Path
import pandas as pd

class Extract:
    def __init__(self, url, headers=None, params=None):
        self.url = url
        self.headers = headers
        self.params = params
        
    def download_gme_data(self, append=False):
        tmp_destination = Path(Path.cwd(), "tmp", "gme_data.csv")
        res = req.get(self.url, headers=self.headers, params=self.params)
        if res.status_code == 200:    
            if append:
                mode = "a"
            else:
                mode = "w"
                        
            with open(tmp_destination, f"{mode}b") as file:
                file.write(res.content)
                print("GME data saved successfully!")
        else:
            print("Failed to fetch data. Status code:", res.status_code)


    def read_gme_data(self) -> pd.DataFrame:
        source = Path(Path.cwd(), "tmp", "gme_data.csv")
        df = pd.read_csv(source)
        return df