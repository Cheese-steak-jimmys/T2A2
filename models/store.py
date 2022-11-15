from marshmallow import fields

from init import db, ma


class Store(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    suburb = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer)

    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))

    items = db.relationship("Item", back_populates="store", cascade="all, delete")
    orders = db.relationship("Order", back_populates="store", cascade="all, delete")


class CustomerSchema(ma.Schema):
    items = fields.List(fields.Nested("ItemSchema", exclude=["store"]))
    orders = fields.List(fields.Nested("OrderSchema", exclude=["store"]))

    class Meta:
        fields = (
            "id",
            "suburb",
            "email",        
            "phone",     
            "items",
            "orders",
           
        )
        # ordered = True