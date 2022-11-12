from flask import Blueprint

from init import db
from models.item import Item, ItemSchema

items_bp = Blueprint("items", __name__, url_prefix="/items")


@items_bp.route("/")
# @jwt_required()
def all_items():
    # return 'These are your items.'
    # if not authorized():
    #     return {'ERROR': 'You must be an administrator to have access'}, 401

    stmt = db.select(Item).order_by(Item.brand.desc(), Item.price)
    items = db.session.scalars(stmt)
    return ItemSchema(many=True).dump(items)


@items_bp.route('/int:id>')
def one_item(id):
    stmt = db.select(Item).filter_by(id=id)
    item = db.session.scalar(stmt)
    if item:
        return ItemSchema(many=True).dump(item)
    else:
        return {'ERROR': f'No item found with ID {id}'}, 404


