import pandas as pd
from DWH import engine

class Load:
    def to_datawarehouse(self, data: pd.DataFrame, table_name: str):                                  
        data.to_sql(table_name, engine, if_exists="append", index=False)        
        
        