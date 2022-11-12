from flask import Blueprint, request
from datetime import date
from init import db
from models.order import Order, OrderSchema

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")


@orders_bp.route("/")
# @jwt_required()
def all_orders():
    return 'Dear customer, here is your order.'

@orders_bp.route('/new/order/', methods=['POST'])
def new_order():
        # create a new order
        order = Order(
            date = date.today(),
            customer_id = request.json['customers_id'],
            item_id = request.json['items_id'],
            delivery = request.json['delivery'],
            total_amount = db.Foreign_key("price")
        )
            # Add user to database
        db.session.add(order)
        db.session.commit()

        # response
        return OrderSchema.dump(Order), 201
  
