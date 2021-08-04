from flask_project import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        user = {
            "id":self.id,
            "usename": self.username,
            "email":self.email,
        }
        return f"{user}"
