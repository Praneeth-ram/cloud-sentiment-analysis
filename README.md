# Cloud-Based Sentiment Analysis Platform

A cloud-deployable app that analyzes the sentiment of text using NLP and returns results via a FastAPI backend and Streamlit frontend.

## Features
- Sentiment classification (Positive/Negative/Neutral)
- FastAPI-based backend
- Streamlit-based frontend
- Dockerized for deployment on AWS/GCP/Heroku

## Getting Started

### Run Backend
```bash
cd backend
uvicorn main:app --reload
```

### Run Frontend
```bash
cd frontend
streamlit run app.py
```
