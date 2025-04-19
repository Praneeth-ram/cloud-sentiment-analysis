FROM python:3.9

WORKDIR /app

COPY backend/ /app/backend/
COPY frontend/ /app/frontend/

RUN pip install fastapi uvicorn textblob streamlit requests

EXPOSE 8000

CMD uvicorn backend.main:app --host 0.0.0.0 --port 8000
