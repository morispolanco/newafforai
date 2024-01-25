import streamlit as st
import requests

# API endpoint and credentials
API_URL = "https://api.afforai.com/api/api_completion"
API_KEY = "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e"
SESSION_ID = "65489d7c9ad727940f2ab26f"

def ask_affo(question):
  """
  Sends a question to the AffoRAI API and returns the response.
  """
  payload = {
    "apiKey": API_KEY,
    "sessionID": SESSION_ID,
    "history": [{"role": "user", "content": question}],
    "powerful": True,
    "google": True,
  }
  response = requests.post(API_URL, json=payload)
  return response.json()["completions"][0]["text"]

st.title("Pregunta sobre las leyes de Guatemala")

# Input field for the user's question
user_question = st.text_input("¿Qué pregunta tienes sobre las leyes de Guatemala?")

# Button to trigger the AffoRAI query
if st.button("Preguntar"):
  # Send the question to AffoRAI and get the response
  affo_response = ask_affo(user_question)

  # Display the response with legal sources
  st.success("Respuesta:")
  st.markdown(affo_response)
  st.markdown("---")
  st.info("Fuentes legales:")
  # TODO: Extract and display legal sources from the AffoRAI response

st.markdown("---")
st.markdown("**Disclaimer:** Esta app no reemplaza el asesoramiento legal profesional. Siempre consulte con un abogado para obtener asesoramiento específico.")

