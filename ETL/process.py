from ETL.extract import Extract
from ETL.transform import Transform
from ETL.load import Load

class Process:
    def __init__(self, startdate: str, enddate: str) -> None:
        self.startdate = startdate
        self.enddate = enddate
        
    def run(self):
        try:
            print("ETL extraction phase started")
            extract = Extract(self.startdate, self.enddate)
            extract.download_gme_data()
            print("Data downloaded successfully")
            df = extract.read_gme_data()
            print("Data read successfully")
            print("ETL extraction phase ended")
            
            print("ETL transformation phase started")
            transform = Transform(data=df)
            transform.perform_data_transformations()
            print("Data transformed successfully")
            transformed_data = transform.data
            print("ETL transformation phase ended")
            
            print("ETL load phase started")
            load = Load()
            load.to_datawarehouse(data=transformed_data, table_name="GME")
            print("Data loaded successfully")
            print("ETL load phase ended")
        except Exception as e:
            print("An error occurred during the ETL process")
            print(e)
        