import streamlit as st
import requests

# URL del backend de FastAPI
FASTAPI_URL = "http://127.0.0.1:8000/ask/"

# Título y descripción
st.title("Sócrates")
st.write("Escribe tu pregunta y Sócrates te responderá.")

# Entrada del usuario
user_input = st.text_input("Escribe tu pregunta:")

# Botón para enviar la pregunta
if st.button("Enviar"):
    if user_input:
        # Hacer solicitud POST a FastAPI
        response = requests.post(FASTAPI_URL, json={"question": user_input})
        
        # Mostrar la respuesta
        if response.status_code == 200:
            st.write("**Sócrates responde:**")
            st.write(response.json()['response'])
        else:
            st.write("Error al obtener respuesta.")
    else:
        st.write("Por favor, escribe una pregunta.")
