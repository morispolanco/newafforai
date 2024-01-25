import streamlit as st
import requests

# Define the API endpoint and your API key.
api_endpoint = "https://api.afforai.com/api/api_completion"
api_key = "your_api_key"

# Create a Streamlit app.
st.title("Guatemala Legal Information App")

# Create a text input field for the user to enter their question.
user_question = st.text_input("Ask a question about the laws of Guatemala:", placeholder="What are the laws regarding marriage in Guatemala?")

# Create a button for the user to submit their question.
if st.button("Get Answer"):
    # Prepare the request body.
    request_body = {
        "apiKey": api_key,
        "sessionID": "65489d7c9ad727940f2ab26f",
        "history": [
            {"role": "user", "content": user_question}
        ],
        "powerful": True,
        "google": True,
    }

    # Send the request to the API.
    response = requests.post(api_endpoint, json=request_body)

    # Extract the answer from the API response.
    answer = response.json()["candidates"][0]["output"]

    # Display the answer to the user.
    st.write(f"**Answer:** {answer}")

    # Display the source of the answer.
    st.write(f"**Source:** {response.json()['candidates'][0]['source']}")
