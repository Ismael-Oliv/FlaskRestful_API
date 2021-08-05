from flask import jsonify
from flask_project.utils.jwt_generator import Jwt_Genator
from flask_restful import Resource, reqparse, abort
from flask_project.model import User, UserSchema
from flask_project import bcrypt


class AuthenticateUserController(Resource):
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument("email", type=str)
        parser.add_argument("password", type=str)
        parser.add_argument("token", type=str, location="headers")

        args = parser.parse_args()
        exits_user = User.query.filter_by(email=args.email).first()

        if not exits_user:
            abort(403, error="Dados incorretos/Não encontrado")

        matched_password = bcrypt.check_password_hash(exits_user.password, args.password)
        if not matched_password:
            abort(403, error="Senha incorreta")

        user = UserSchema().dump(exits_user)
        del user["password"]
        encode = Jwt_Genator.generator("")

        return {"user": user, "token": encode}
