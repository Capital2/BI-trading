FROM python:3.9-bookworm

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "3000"]