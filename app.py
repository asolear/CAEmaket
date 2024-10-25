# cred = credentials.Certificate("prueba-440b0-firebase-adminsdk-u5o4x-c9a9493686.json")

        # const firebaseConfig = {
        #     apiKey: "AIzaSyDY1GhUR47WGpJcNhpq2gPTOKIyCJ1_oaw",
        #     authDomain: "prueba-440b0.firebaseapp.com",
        #     databaseURL: "https://prueba-440b0-default-rtdb.europe-west1.firebasedatabase.app",
        #     projectId: "prueba-440b0",
        #     storageBucket: "prueba-440b0.appspot.com",
        #     messagingSenderId: "799443941595",
        #     appId: "1:799443941595:web:6d12fa146ec1308a20f4fe",
        #     measurementId: "G-W9NBWXRCCF"
        # };



import streamlit as st
from firebase_config import auth

# Títulos y Descripción
st.title("Autenticación con Firebase")
st.write("Inicia sesión o regístrate")

# Formulario de Registro
def registro():
    email = st.text_input("Correo Electrónico")
    password = st.text_input("Contraseña", type="password")
    
    if st.button("Registrar"):
        try:
            auth.create_user_with_email_and_password(email, password)
            st.success("Registro exitoso!")
        except Exception as e:
            st.error(e)

# Formulario de Inicio de Sesión
def inicio_sesion():
    email = st.text_input("Correo Electrónico", key="login_email")
    password = st.text_input("Contraseña", type="password", key="login_password")
    
    if st.button("Iniciar Sesión"):
        try:
            auth.sign_in_with_email_and_password(email, password)
            st.success("Inicio de sesión exitoso!")
        except Exception as e:
            st.error(e)

# Navegación
opcion = st.selectbox("Selecciona una opción", ["Iniciar Sesión", "Registrar"])

if opcion == "Registrar":
    registro()
else:
    inicio_sesion()
