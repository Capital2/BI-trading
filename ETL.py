from ETL.extract import Extract


def ETL():    
    url = "https://www.marketwatch.com/investing/stock/gme/downloaddatapartial"
    params = {
        "startdate": "11/13/2022",
        "enddate": "11/13/2023",
        "daterange": "d30",
        "frequency": "p1d",
        "csvdownload": "true",
        "downloadpartial": "false",
        "newdates": "false",
    }
    extract = Extract(url, params=params)
    extract.get_data()
    
if __name__ == "__main__":
    ETL()