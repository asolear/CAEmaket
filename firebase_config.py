#     "apiKey": "AIzaSyDY1GhUR47WGpJcNhpq2gPTOKIyCJ1_oaw",
#     "authDomain": "prueba-440b0.firebaseapp.com",
#     "databaseURL": "https://prueba-440b0-default-rtdb.europe-west1.firebasedatabase.app",
#     "projectId": "prueba-440b0",
#     "storageBucket": "prueba-440b0.appspot.com",
#     "messagingSenderId": "799443941595",
#     "appId": "1:799443941595:web:6d12fa146ec1308a20f4fe",
#     "measurementId": "G-W9NBWXRCCF"


import pyrebase

config = {
    "apiKey": "AIzaSyDY1GhUR47WGpJcNhpq2gPTOKIyCJ1_oaw",
    "authDomain": "prueba-440b0.firebaseapp.com",
    "databaseURL": "https://prueba-440b0-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "prueba-440b0",
    "storageBucket": "prueba-440b0.appspot.com",
    "messagingSenderId": "799443941595",
    "appId": "1:799443941595:web:6d12fa146ec1308a20f4fe",
    "measurementId": "G-W9NBWXRCCF",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

