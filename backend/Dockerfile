FROM python:3.9-bookworm

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip 

RUN pip install --upgrade pip wheel==0.38.4 && pip install --no-cache-dir -r requirements.txt

COPY ./app .

HEALTHCHECK CMD curl --fail http://localhost:3000/health

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]