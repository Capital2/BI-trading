FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY ./app .

HEALTHCHECK CMD curl --fail http://localhost:3000/health

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]