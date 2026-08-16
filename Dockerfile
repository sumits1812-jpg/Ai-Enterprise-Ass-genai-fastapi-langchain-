FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ..

CMD["sh","-c",uvicorn sqlfastapi:app --host0.0.0.0 --port${PORT:-8000}"]

