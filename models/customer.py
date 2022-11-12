from init import db
# from marshmallow import fields

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.integer(10), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    membership = db.Column(db.boolean)