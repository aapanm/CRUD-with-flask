import json
from flask import jsonify
from model.gcpFirestore import db

user_ref = db.collection("user-crud")


# gets a specific or all users from firestore
def getUsersService(request, userId):
    try:
        user_id = userId
        if user_id:
            user = user_ref.document(user_id).get()
            return jsonify(user.to_dict()), 200
        else:
            users = [doc.to_dict() for doc in user_ref.stream()]
            return jsonify(users), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


# stores user data in the firestore
def createUserService(request):
    try:
        userId = request.json["userId"]
        user_ref.document(str(userId)).set(request.json)
        return jsonify({"success": True, "data": request.json}), 201
    except Exception as e:
        return f"An Error Occurred: {e}", 400


# updates user in the firestore
def updateUserService(request):
    try:
        userId = request.json["userId"]
        user_ref.document(str(userId)).update(request.json)
        return jsonify({"success": True, "data": request.json}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"


# deletes user in the firestore
def deleteUserService(request, userId):
    try:
        user_id = userId
        user_ref.document(user_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occurred: {e}"
