from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:docker@localhost:5432/flask_restful"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
api = Api(app)

from flask_project import routes



