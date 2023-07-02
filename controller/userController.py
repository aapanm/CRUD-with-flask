from flask import jsonify, make_response, request
from service.userService import (
    getUsersService,
    createUserService,
    updateUserService,
    deleteUserService,
)


def getUsers():
    response = getUsersService(request)
    return response


def creatUser():
    response = createUserService(request)
    return response


def updateUser():
    response = updateUserService(request)
    return response

def deleteUser():
    response = deleteUserService(request)
    return response