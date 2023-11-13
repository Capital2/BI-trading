import requests as req
from pathlib import Path

class Extract:
    def __init__(self, url, headers=None, params=None):
        self.url = url
        self.headers = headers
        self.params = params
        
    def get_data(self):
        tmp_destination = Path(Path.cwd(), "tmp", "gme_data.csv")
        res = req.get(self.url, headers=self.headers, params=self.params)
        if res.status_code == 200:            
            with open(tmp_destination, "wb") as file:
                file.write(res.content)
                print("GME data saved successfully!")
        else:
            print("Failed to fetch data. Status code:", res.status_code)
