from flask import Blueprint, request
from datetime import date
from init import db
from models.order import Order, OrderSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")

@orders_bp.route("/")
# @jwt_required()
def get_all_orders():
    stmt = db.select(Order)
    orders = db.session.scalars(stmt)
    return OrderSchema(many=True).dump(orders)

orders_bp.route("/new", methods=["POST"])
@jwt_required()
def create_order():
    # Create a new Card model instance
    data = OrderSchema().load(request.json)

    order = Order(
        customer_id = get_jwt_identity(),
        item_id = data["items_id"],
        date = date.today(),
        delivery = data["delivery"]
       
    )
    # Add and commit card to DB
    db.session.add(order)
    db.session.commit()
    # Respond to client
    return OrderSchema().dump(order), 201

@orders_bp.route("/<int:id>")
def get_one_order(id):
    stmt = db.select(Order).filter_by(id=id)
    order = db.session.scalar(stmt)
    if order:
        return OrderSchema(many=False).dump(order)
    else:
        return {" ! ERROR ": f"NOT FOUND. Sorry, there\'s no order with ID {id}, please try another"}, 404

@orders_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_one_order(id):
    stmt = db.select(Order).filter_by(id=id)
    order = db.session.scalar(stmt)
    if order:
        order.items = request.json.get('title') or order.items
        order.delivery = request.json.get('delivery') or order.delivery
        db.session.commit()     
        return OrderSchema().dump(order)
    else:
        return {" ! ERROR ": f"NOT FOUND. Sorry, there\'s no order with ID {id}, please try another"}, 404

# , "DELETE"]