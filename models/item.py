from marshmallow import fields

from init import db, ma


class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    department = db.Column(db.String, nullable=True)
    price = db.Column(db.Float, nullable=False)
    in_stock = db.Column(db.Boolean, nullable=False)
    on_promotion = db.Column(db.Boolean, default=False)

    # order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    

    store = db.relationship("Store", back_populates="items")
    orders = db.relationship("Order", back_populates="items", cascade="all, delete")


class ItemSchema(ma.Schema):
    stores = fields.Nested("StoreSchema", only=["store_id"])
    orders = fields.List(fields.Nested("OrderSchema", exclude=["item"]))

    class Meta:
        fields = (
            "id",
            "stores"
            "brand",
            "description",
            "department",
            "in_stock",
            "price",
            "on_promotion",
        )
        ordered = True
