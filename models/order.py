from init import db
# from marshmallow import fields

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    delivery = db.Column(db.boolean)

    customer_id = db.Column(db.Integer, db.Foreign_key('customers.id'))
    item_id = db.Column(db.Integer, db.Foreign_key('items.id'))
    store_id = db.Column(db.Integer, db.Foreign_key('stores.db'))

    customer = db.relationship("Customer", back_populates="orders")
    item = db.relationship("Item", back_populates="orders")
    store = db.relationship("Store", back_populates="orders")

# class OrderSchema(ma.Schema):
#     customer = fields.Nested('CustomerSchema', only=['name', 'email', 'address'])
#     customer = fields.List(fields.Nested('CustomerSchema', exclude=['password']))