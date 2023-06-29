from flask import Blueprint
from controller.userController import getUsers, creatUser, updateUser, deleteUser

blueprint = Blueprint("userRoute", __name__)

blueprint.route("/users", methods=["GET"])(getUsers)
blueprint.route("/user", methods=["POST"])(creatUser)
blueprint.route("/user/<int:userId>", methods=["PATCH"])(updateUser)
blueprint.route("/user/<int:userId>", methods=["DELETE"])(deleteUser)
