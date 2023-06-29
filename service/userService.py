import json


def getUsersService():
    try:
        response = {"data": "All users Data"}
        return response
    except Exception as e:
        return {"Error": e}


def createUserService(data):
    try:
        response = {"data": f"User created with data {data}"}
        return response
    except Exception as e:
        return {"Error": e}


def updateUserService(data):
    try:
        response = {"data": f"User updated with id {data}"}
        return response
    except Exception as e:
        return {"Error": e}


def deleteUserService(data):
    try:
        response = {"data": f"User deleted with id {data}"}
        return response
    except Exception as e:
        return {"Error": e}
