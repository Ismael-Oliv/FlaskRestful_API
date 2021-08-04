from flask_project.controllers.UsersController import UsersController
from flask_project import api


api.add_resource(UsersController, "/home")

