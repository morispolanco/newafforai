import streamlit as st
import requests
import json

# Set the API key and session ID
api_key = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
session_id = "65489d7c9ad727940f2ab26f"

# Create a function to call the API
def call_api(prompt):
    url = "https://api.afforai.com/api/api_completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "sessionID": session_id,
        "history": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "powerful": True,
        "google": True
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            # Process the response
            answer = response.json()["candidates"][0]["output"]
            citations = response.json()["candidates"][0]["citations"]
            return answer, citations
        else:
            st.error(f"Error: {response.status_code}")
            return None, None
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

# Create the Streamlit app
st.title("Guatemala Law Q&A")
st.write("Ask me any question about the laws of Guatemala, and I'll give you the answer, along with the relevant legal citations.")

# Get the user's question
question = st.text_input("Ask me a question:")

# Input validation
if not question or not question.strip():
    st.warning("Please enter a valid question.")
else:
    # Call the API
    answer, citations = call_api(question)

    # Display the answer and the citations
    if answer is not None and citations is not None:
        st.write("**Answer:**")
        st.write(answer)
        st.write("\n")
        st.write("**Citations:**")
        for i, citation in enumerate(citations, start=1):
            st.write(f"{i}. {citation}")
