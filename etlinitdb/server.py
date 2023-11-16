from fastapi import FastAPI

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Creating our singleton instance of the MarketActivityCube class
    pass

@app.get("/")
def read_root():
    return {"Hello": "World"}

