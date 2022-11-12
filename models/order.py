from marshmallow import fields

from init import db, ma


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    delivery = db.Column(db.Boolean, default=False)

    customer_id = db.Column(db.Integer, db.Foreign_key("customers.id"), nullable=False)
    item_id = db.Column(db.Integer, db.Foreign_key("items.id"), nullable=False)
    total_amount = db.Column(db.Integer, db.Foreign_key("price"), nullable=False)

    customer = db.relationship("Customer", back_populates="orders")
    items = db.relationship("Item", back_populates="orders", cascade="all, delete")


class OrderSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["name", "email"])
    card = fields.Nested("CardSchema")

    class Meta:
        fields = ("id", "date", "customer_id", "item_id", "delivery", "total_amount")
        ordered = True


# class OrderSchema(ma.Schema):
#     customer = fields.Nested('CustomerSchema', only=['name', 'email', 'address'])
#     customer = fields.List(fields.Nested('CustomerSchema', exclude=['password']))
