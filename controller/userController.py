from flask import jsonify, make_response, request

# importing service functions
from service.userService import (
    getUsersService,
    createUserService,
    updateUserService,
    deleteUserService,
)


# function to call service for getting users forwarding incoming request
# also forwards requests with user id in the query parameter to fetch specific user
def getUsers():
    response = getUsersService(request)
    return response


# function to call service for creating user forwarding incoming request with json body
def creatUser():
    response = createUserService(request)
    return response


# function to call service for updating user forwarding incoming request with json body
def updateUser():
    response = updateUserService(request)
    return response


# function to call service for deleting user forwarding incoming request with user id in the query parameter
def deleteUser():
    response = deleteUserService(request)
    return response
