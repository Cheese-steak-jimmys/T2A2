from marshmallow import fields

from init import db, ma


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer)
    password = db.Column(db.String, nullable=False)
    is_member = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)

    # order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), nullable=False)

    store = db.relationship("Store", back_populates="customer", cascade="all, delete")
    orders = db.relationship("Order", back_populates="customer", cascade="all, delete")


class CustomerSchema(ma.Schema):
    store = fields.List(fields.Nested("StoreSchema", exclude=["customer"]))
    orders = fields.List(fields.Nested("OrderSchema", exclude=["customer"]))

    class Meta:
        fields = (
            "id",
            "name",
            "email",
            "address",
            "phone",
            "password",
            "is_member",
            "items",
            "orders",
            "is_admin",
        )
        # ordered = True
