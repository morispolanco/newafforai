import streamlit as st
import requests

# API key and session ID
api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
session_id = "65489d7c9ad727940f2ab26f"

# Function to call the API
def call_api(question):
    url = "https://api.afforai.com/api/api_completion"
    data = {
        "apiKey": api_key,
        "sessionID": session_id,
        "history": [{"role": "user", "content": question}],
        "powerful": True,
        "google": True
    }
    response = requests.post(url, json=data)
    return response.json()['choices'][0]['message']['content']

# User input
question = st.text_input("Ask a question about Guatemalan laws:")

# Display the answer
if question:
    answer = call_api(question)
    st.write(answer)
