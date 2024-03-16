from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db=SQLAlchemy()
hash=generate_password_hash("password")

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),unique=True,nullable=False)
    name1=db.Column(db.String(30),unique=True,nullable=False)
    mail=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(30),unique=True,nullable=False)

    def __repr__(self):
        return f'{self.name} {self.name2}'