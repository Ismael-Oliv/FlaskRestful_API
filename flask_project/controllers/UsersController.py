from flask import jsonify
from flask_restful import Resource, abort, reqparse
from flask_project.model import User
from flask_project import db, bcrypt
from flask_project.serializer import serializer


class UsersController(Resource):
    @staticmethod
    def get():
        all_users = User.query.all()
        return jsonify([*map(serializer, all_users)])

    @staticmethod
    def post():
        parser = reqparse.RequestParser()

        parser.add_argument("username", type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        exists_user = User.query.filter_by(email=args.email).first()

        if exists_user:
            abort(403, error="Usuario já cadastrado")

        try:
            rashed_password = bcrypt.generate_password_hash(args.password, 4)
            user = User(
                username=args.username,
                email=args.email,
                password=rashed_password
            )

            db.session.add(user)
            db.session.commit()

            created_user = User.query.filter_by(email=args.email).all()

            return jsonify([*map(serializer, created_user)])

        except Exception as Ex:
            print(Ex)
            abort(500, error="Erro ao cadastrar usuario")
