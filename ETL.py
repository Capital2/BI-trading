from ETL.extract import Extract


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
    
if __name__ == "__main__":
    ETL()