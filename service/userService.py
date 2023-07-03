import json
from flask import jsonify

# from firebase_admin import credentials, firestore, initialize_app
# cred = credentials.Certificate("path to key.json")
# default_app = initialize_app(cred)
# db = firestore.client()

from google.cloud import firestore

db = firestore.Client(project="user-crud-391515")

user_ref = db.collection("user-crud")


def getUsersService(request):
    try:
        user_id = request.args.get("userId")
        if user_id:
            user = user_ref.document(user_id).get()
            return jsonify(user.to_dict()), 200
        else:
            users = [doc.to_dict() for doc in user_ref.stream()]
            return jsonify(users), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


def createUserService(request):
    try:
        userId = request.json["userId"]
        user_ref.document(str(userId)).set(request.json)
        return jsonify({"success": True, "data": request.json}), 201
    except Exception as e:
        return f"An Error Occurred: {e}", 400


def updateUserService(request):
    try:
        userId = request.json["userId"]
        user_ref.document(str(userId)).update(request.json)
        return jsonify({"success": True, "data": request.json}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


def deleteUserService(request):
    try:
        todo_id = request.args.get("userId")
        user_ref.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"
