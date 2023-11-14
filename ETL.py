from ETL.extract import Extract
from ETL.transform import Transform
from ETL.load import Load


def ETL():    
    url = "https://www.marketwatch.com/investing/stock/gme/downloaddatapartial"
    params = {
        "startdate": "11/10/2022 00:00:00",
        "enddate": "11/10/2023 00:00:00",
        "daterange": "d30",
        "frequency": "p1d",
        "csvdownload": "true",
        "downloadpartial": "false",
        "newdates": "false",
    }
    
    extract = Extract(url, params=params)
    extract.download_gme_data(append=False)
    df = extract.read_gme_data()
    print("data extracted")
    print(df)
    
    transform = Transform(df)
    transform.perform_data_transformations()
    print("data transformed")
    print(transform.data)
    
    load = Load()
    load.to_datawarehouse(transform.data, "GME")
    
if __name__ == "__main__":
    ETL()