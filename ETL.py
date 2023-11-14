from ETL.process import Process

def ETL():    
    startdate = "11/10/2022 00:00:00"
    enddate = "11/10/2023 00:00:00"
    process = Process(startdate=startdate, enddate=enddate)
    process.run()
    
if __name__ == "__main__":
    ETL()