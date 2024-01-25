import streamlit as st
import requests

# Definir la URL de la API
url = "https://api.afforai.com/api/api_completion"

# Configurar los parámetros requeridos por la API
params = {
    "apiKey": "fcbfdfe8-e9ed-41f3-a7d8-b6587538e84e",
    "sessionID": "65489d7c9ad727940f2ab26f",
    "history": [
        {
            "role": "user",
            "content": "What is AI?"
        }
    ],
    "powerful": True,
    "google": True
}

# Realizar la llamada a la API para obtener la respuesta
response = requests.post(url, json=params)
data = response.json()

# Mostrar la respuesta en la interfaz de Streamlit
st.write("Respuesta:", data["completions"][0]["choices"][0]["text"])

# Citando la fuente
st.write("Fuente:", data["completions"][0]["choices"][0]["metadata"]["source"])
