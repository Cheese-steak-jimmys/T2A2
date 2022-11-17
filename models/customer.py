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
    acc_active = db.Column(db.Boolean, default=True, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))

    store = db.relationship("Store", back_populates="customers")
    orders = db.relationship("Order", back_populates="customer", cascade="all, delete")


class CustomerSchema(ma.Schema):
    store = fields.Nested("StoreSchema")
    orders = fields.List(fields.Nested("OrderSchema", exclude=["customer"]))

    class Meta:
        fields = (
            "id",
            "store",
            "name",
            "email",
            "address",
            "phone",
            "password",
            "is_member",
            "is_admin"
            "orders"
        )
        ordered = True
