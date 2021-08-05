from flask_project.controllers.CreateUserController import CreateUserController
from flask_project.controllers.AuthenticateUserController import AuthenticateUserController
from flask_project import api


api.add_resource(CreateUserController, "/home/create")
api.add_resource(AuthenticateUserController, "/home/login")

