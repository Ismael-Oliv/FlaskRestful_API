from flask_project.controllers.CreateUserController import CreateUserController
from flask_project import api


api.add_resource(CreateUserController, "/home/create")

