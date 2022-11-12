from flask import Blueprint

# from init import db

items_bp = Blueprint("items", __name__, url_prefix="/items")


@items_bp.route("/")
# @jwt_required()
def all_items():
    return 'These are your items.'
    # if not authorized():
    #     return {'ERROR': 'You must be an administrator to have access'}, 401

    # stmt = db.select(Item).order_by(Item.brand.description(), Item.price)
    # items = db.session.scalars(stmt)
    # return ItemSchema(many=True).dump(items)
