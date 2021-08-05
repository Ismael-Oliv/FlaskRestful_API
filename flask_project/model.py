import uuid

from sqlalchemy.dialects.postgresql import UUID
from flask_project import db, marsh


class User(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4().hex, unique=True, nullable=False)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        user = {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

        return f"{user}"


class UserSchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
