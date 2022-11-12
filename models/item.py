from init import db

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String, (50), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    inventory = db.Column(db.Integer, nullable=False)
    promotion = db.Column(db.Boolean)
