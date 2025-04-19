import streamlit as st
import requests

st.title("💬 Sentiment Analysis App")
text = st.text_area("Enter your text here:")

if st.button("Analyze"):
    response = requests.post("http://localhost:8000/predict", json={"text": text})
    result = response.json()
    st.markdown(f"**Sentiment:** {result['sentiment']}")
    st.markdown(f"**Confidence:** {result['confidence']}%")
