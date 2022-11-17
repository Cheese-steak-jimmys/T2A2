from marshmallow import fields

from init import db, ma


class Store(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    suburb = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer)
  
    items = db.relationship("Item", back_populates="store", cascade="all, delete")
    customers = db.relationship("Customer", back_populates="store", cascade="all, delete")
    orders = db.relationship("Order", back_populates="store", cascade="all, delete")
    
class StoreSchema(ma.Schema):
    items = fields.List(fields.Nested("ItemSchema", exclude=["stores"]))
    orders = fields.List(fields.Nested("OrderSchema"))
    customers = fields.List(fields.Nested("CustomerSchema", exclude=["password"]))

    class Meta:
        fields = ("id", "suburb", "email", "phone", "customers", "items", "orders")
        # ordered = True
