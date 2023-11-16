from ETL.process import Process as ETLProcess
from multiprocessing import Process
from DWH import Base, engine

def init_db():
    Base.metadata.create_all(engine)
    

def ETL():
    # Process parameters
    startdate = "11/10/2022 00:00:00"
    enddate = "11/10/2023 00:00:00"
    headers = None
    params = {
        "startdate": startdate,
        "enddate": enddate,
        "daterange": "d30",
        "frequency": "p1d",
        "csvdownload": "true",
        "downloadpartial": "false",
        "newdates": "false",
    }
    

    # Different shares urls
    gme_url = "https://www.marketwatch.com/investing/stock/gme/downloaddatapartial" # GameStop Corp. Cl A
    atnfw_url = "https://www.marketwatch.com/investing/stock/atnfw/downloaddatapartial" # 180 Life Sciences Corp. Wt
    fisb_url = "https://www.marketwatch.com/investing/stock/fisb/downloaddatapartial" # 1st Constitution Bancorp
    ascbr_url = "https://www.marketwatch.com/investing/stock/ascbr/downloaddatapartial" # A SPAC II Acquisition Corp. Rt
    acco_url = "https://www.marketwatch.com/investing/stock/acco/downloaddatapartial" # Acco Brands Corp.
    
    # Running the different ETL process in parallel
    gme_process = ETLProcess(url=gme_url, headers=headers, params=params, name="GameStop Corp. Cl A", share="GME")
    atnfw_process = ETLProcess(url=atnfw_url, headers=headers, params=params, name="180 Life Sciences Corp. Wt", share="ATNFW")
    fisb_process = ETLProcess(url=fisb_url, headers=headers, params=params, name="1st Constitution Bancorp", share="FISB")
    ascbr_process = ETLProcess(url=ascbr_url, headers=headers, params=params, name="A SPAC II Acquisition Corp. Rt", share="ASCBR")
    acco_process = ETLProcess(url=acco_url, headers=headers, params=params, name="Acco Brands Corp.", share="ACCO")
    
    # Create instances of the Process class
    gme_process = Process(target=gme_process.run)
    atnfw_process = Process(target=atnfw_process.run)
    fisb_process = Process(target=fisb_process.run)
    ascbr_process = Process(target=ascbr_process.run)
    acco_process = Process(target=acco_process.run)

    # Start each process
    gme_process.start()
    atnfw_process.start()
    fisb_process.start()
    ascbr_process.start()
    acco_process.start()

    # Wait for each process to finish
    gme_process.join()
    atnfw_process.join()
    fisb_process.join()
    ascbr_process.join()
    acco_process.join()


if __name__ == "__main__":
    try:
        init_db()
        print("Database initialized successfully")
    except Exception as e:
        print("Database initialization failed")
        print(e)
    ETL()
