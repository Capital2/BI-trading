from fastapi import FastAPI, HTTPException, status
import asyncio
import subprocess
from pydantic import BaseModel

app = FastAPI()

class AppState:
    process: asyncio.subprocess.Process = None

class HealthCheck(BaseModel):
    status: str = "OK"

app.state = AppState()

@app.on_event("startup")
async def startup_event():
    app.state.process = await asyncio.create_subprocess_exec(
        "python", "ETLmain.py",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    try:
        while True:
            output = await asyncio.gather(
                app.state.process.stdout.readline(),
                app.state.process.stderr.readline(),
            )
            if output[0]:
                print(f"stdout: {output[0].decode()}")
            if output[1]:
                print(f"stderr: {output[1].decode()}")

            if app.state.process.returncode is not None:
                if app.state.process.returncode == 1:
                    output = await asyncio.gather(
                        app.state.process.stdout.read(),
                        app.state.process.stderr.read(),
                    )
                    print(f"stderr: {output[1].decode()}")

                if app.state.process.returncode == 0:
                    output = await asyncio.gather(
                        app.state.process.stdout.read(),
                        app.state.process.stderr.read(),
                    )
                    print(f"stderr: {output[0].decode()}")
                break

        print(f"Process exited with return code {app.state.process.returncode}")

    except asyncio.CancelledError:
        app.state.process.terminate()
        await app.state.process.communicate()


@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:

    if app.state.process.returncode == 0:
        return HealthCheck(status="OK")
    raise Exception("init process still on going or is failing.")