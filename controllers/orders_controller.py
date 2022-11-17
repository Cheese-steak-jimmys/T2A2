from datetime import date

from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from controllers.auth_controller import authorize
from init import db
from models.order import Order, OrderSchema

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")

# select all orders
@orders_bp.route("/")
@jwt_required()
def get_all_orders():
    if not authorize():
        return {'error': 'You must be an admin'}, 401

    stmt = db.select(Order)
    orders = db.session.scalars(stmt)
    return OrderSchema(many=True).dump(orders)


# select an order with order_id
@orders_bp.route("/<int:id>")
def get_one_order(id):
    stmt = db.select(Order).filter_by(id=id)
    order = db.session.scalar(stmt)
    if order:
        return OrderSchema(many=False).dump(order)
    else:
        return {
            " ! ERROR ": f"NOT FOUND. Sorry, there's no order with ID {id}, please try another"
        }, 404


@orders_bp.route("/new", methods=["POST"])
@jwt_required()
def create_order():
    # Create a new order
    data = OrderSchema().load(request.json)
    
    order = Order(
        customer_id=data["customer_id"],
        item_id=data["item_id"],
        date=date.today(),
        delivery=data["delivery"],
    )
    # Add and commit order to DB
    db.session.add(order)
    db.session.commit()
    # Respond to client
    return OrderSchema().dump(order), 201


# append/alter an order
@orders_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_one_order(id):
    stmt = db.select(Order).filter_by(id=id)
    order = db.session.scalar(stmt)
    if order:
        order.items = request.json.get("title") or order.items
        order.delivery = request.json.get("delivery") or order.delivery
        db.session.commit()

        # return altered order
        return OrderSchema().dump(order)
    else:
        return {
            " ! ERROR ": f"NOT FOUND. Sorry, there's no order with ID {id}, please try another"
        }, 404
