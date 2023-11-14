import atoti as tt
import pandas as pd
from dotenv import load_dotenv
import os

class GME_Cube:
    def __init__(self) -> None:
        load_dotenv()
        self.session = tt.Session()
        self.table = None
        self.cube = None
        self.hierarchies = None
        self.measures = None

    def get_gme_table(self):        
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_username = os.getenv("DB_USERNAME")
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME")
        self.table = self.session.read_sql(
            'select date, open, high, low, close, volume, "SMA", "RSI", "OBV" from "GME" g \
            order by date asc;',
            url=f"postgresql://{db_host}:{db_port}/{db_name}?user={db_username}&password={db_password}",         
            table_name="GME",
            keys=["date"],
        )
        
        print(self.table.head())
        print(type(self.table))
        
    def create_cube(self):
        self.cube = self.session.create_cube(self.table, "GME_Cube")
        self.hierarchies = self.cube.hierarchies
        self.measures = self.cube.measures
        
    def get_hierarchies(self):
        return self.hierarchies
    
    def get_measures(self):
        return self.measures




