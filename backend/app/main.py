from setup import app
from fastapi import status
from modules.OLAP.models.market_activity_cube import MarketActivityCube
from modules.OLAP.routers import olap_routes
from pydantic import BaseModel

class HealthCheck(BaseModel):
    status: str = "OK"

@app.on_event("startup")
async def startup_event():
    # Creating our singleton instance of the MarketActivityCube class
    app.state.market_activity_cube = MarketActivityCube()
    
@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    return HealthCheck(status="OK")
# registering the modules routers
app.include_router(olap_routes.router)
