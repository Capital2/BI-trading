from ETL.extract import Extract
from ETL.transform import Transform
from ETL.load import Load

class Process:
    def __init__(self, url: str, headers: dict, params: dict, name: str, share: str) -> None:
        self.url = url
        self.headers = headers
        self.params = params
        self.name = name
        self.share = share
        
    def run(self):
        try:
            print("ETL extraction phase started")
            extract = Extract(url=self.url, headers=self.headers, params=self.params)
            extract.download_share_data(share=self.share)
            print("Share data downloaded successfully")
            df = extract.read_share_data()
            print("Share data read successfully")
            print("ETL extraction phase ended")
            
            print("ETL transformation phase started")
            transform = Transform(data=df, name=self.name, share=self.share)
            transform.perform_data_transformations()
            print("Data transformed successfully")
            transformed_data = transform.data
            print("ETL transformation phase ended")
            
            print("ETL load phase started")
            load = Load()
            load.to_datawarehouse(data=transformed_data, table_name="market_activity")
            print("Data loaded successfully")
            print("ETL load phase ended")
        except Exception as e:
            print("An error occurred during the ETL process")
            print(e)
        