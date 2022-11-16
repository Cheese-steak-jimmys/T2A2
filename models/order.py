from marshmallow import fields

from init import db, ma


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    delivery = db.Column(db.Boolean, default=False)

    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))

    store = db.relationship("Store", back_populates="orders")
    customer = db.relationship("Customer", back_populates="orders")
    items = db.relationship("Item", back_populates="orders", cascade="all, delete")


class OrderSchema(ma.Schema):
    customer = fields.Nested("CustomerSchema", exclude=["password", "is_admin"])
    store = fields.Nested("StoreSchema", exclude=["order"])
    items = fields.List(fields.Nested("ItemSchema", exclude=["in_stock"]))

    class Meta:
        fields = ("id", "customer_id", "store", "date", "items", "delivery")
        ordered = True
