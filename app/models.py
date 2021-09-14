from app.extensions import db


class Users(db.Model):
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(300), nullable=False)
