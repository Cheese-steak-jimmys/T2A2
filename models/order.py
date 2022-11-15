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

    customer = db.relationship("Customer", back_populates="orders", cascade="all, delete")
    items = db.relationship("Item", back_populates="orders", cascade="all, delete")
    store = db.relationship("Store", back_populates="orders", cascade="all, delete")


class OrderSchema(ma.Schema):
    customer = fields.Nested("CustomerSchema", only=["name", "email"])
    items = fields.List(fields.Nested("ItemSchema", exclude=["order"]))
    store = fields.Nested("StoreSchema")

    class Meta:
        fields = (
            "id",
            "customer_id",
            "date",
            "item_id",
            "delivery"
        )
        ordered = True
