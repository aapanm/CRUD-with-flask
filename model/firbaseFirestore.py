# firebase firestore credentials

from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("path to key.json")
default_app = initialize_app(cred)
db = firestore.client()
