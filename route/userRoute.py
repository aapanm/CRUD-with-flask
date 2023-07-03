from flask import Blueprint

# importing controller functions
from controller.userController import getUsers, creatUser, updateUser, deleteUser

# registering current route file as blueprint
blueprint = Blueprint("userRoute", __name__)

# route to get users
blueprint.route("/users", methods=["GET"])(getUsers)

# route to create user
blueprint.route("/user", methods=["POST"])(creatUser)

# route to update user
blueprint.route("/user", methods=["PATCH"])(updateUser)

# route to delete user
blueprint.route("/user", methods=["DELETE"])(deleteUser)
