from textblob import TextBlob
import re

def clean_text(text):
    text = re.sub(r"http\S+|@\S+|#\S+|[^A-Za-z\s]", "", text)
    return text.strip()

def predict_sentiment(text):
    cleaned = clean_text(text)
    blob = TextBlob(cleaned)
    polarity = blob.sentiment.polarity
    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
    confidence = round(abs(polarity) * 100, 2)
    return sentiment, confidence
