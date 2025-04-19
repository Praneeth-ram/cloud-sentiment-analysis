from fastapi import FastAPI
from model.sentiment import predict_sentiment
from schemas.request_response import SentimentRequest, SentimentResponse

app = FastAPI()

@app.post("/predict", response_model=SentimentResponse)
def analyze_sentiment(data: SentimentRequest):
    sentiment, confidence = predict_sentiment(data.text)
    return SentimentResponse(sentiment=sentiment, confidence=confidence)
