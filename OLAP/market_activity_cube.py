import atoti as tt
import pandas as pd
from dotenv import load_dotenv
import os

class MarketActivityCube:
    def __init__(self) -> None:
        load_dotenv()
        self.session = tt.Session()
        self.table = None
        self.cube = None
        self.hierarchies = None
        self.measures = None
        self.levels = None

    def get_table(self):        
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_username = os.getenv("DB_USERNAME")
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME")
        self.table = self.session.read_sql(
            'select * from market_activity;',            
            url=f"postgresql://{db_host}:{db_port}/{db_name}?user={db_username}&password={db_password}",         
            table_name="market_activity",
            keys=["id"],
        )
        
        print(self.table.head())
        print(type(self.table))
        
    def create_cube(self):
        self.cube = self.session.create_cube(self.table, "MarketActivityCube")
        self.hierarchies = self.cube.hierarchies
        self.measures = self.cube.measures
        self.levels = self.cube.levels
        
    def get_hierarchies(self):
        return self.hierarchies
    
    def get_measures(self):
        return self.measures




