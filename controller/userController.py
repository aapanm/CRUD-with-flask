from flask import jsonify, make_response, request
from service.userService import (
    getUsersService,
    createUserService,
    updateUserService,
    deleteUserService,
)


def getUsers():
    response = getUsersService()

    if response.get("data") == None:
        response["success"] = False
        return make_response(jsonify(response), 401)

    response["success"] = True
    return make_response(jsonify(response), 200)


def creatUser():
    response = createUserService(request.get_json())

    if response.get("data") == None:
        response["success"] = False
        return make_response(jsonify(response), 401)

    response["success"] = True
    return make_response(jsonify(response), 200)


def updateUser(userId):
    response = updateUserService(userId)

    if response.get("data") == None:
        response["success"] = False
        return make_response(jsonify(response), 401)

    response["success"] = True
    return make_response(jsonify(response), 200)


def deleteUser(userId):
    response = deleteUserService(userId)

    if response.get("data") == None:
        response["success"] = False
        return make_response(jsonify(response), 401)

    response["success"] = True
    return make_response(jsonify(response), 200)
