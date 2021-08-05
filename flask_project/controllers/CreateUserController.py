from flask import jsonify
from flask_restful import Resource, abort, reqparse
from flask_project.model import User, UserSchema
from flask_project import db, bcrypt


class CreateUserController(Resource):

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
            rashed_password = bcrypt.generate_password_hash(args.password).decode("utf-8")
            user = User(
                username=args.username,
                email=args.email,
                password=rashed_password
            )

            db.session.add(user)
            db.session.commit()

            created_user = User.query.filter_by(email=args.email).all()
            new_user = UserSchema(many=True).dump(created_user)

            return jsonify(new_user)

        except Exception as Ex:
            print(Ex)
            abort(500, error="Erro ao cadastrar usuario")
