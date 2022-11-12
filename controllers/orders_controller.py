from flask import Blueprint

# from init import db

orders_bp = Blueprint("orders", __name__, url_prefix="/orders")


@orders_bp.route("/")
# @jwt_required()
def all_items():
    return 'Dear customer, here is your order.'