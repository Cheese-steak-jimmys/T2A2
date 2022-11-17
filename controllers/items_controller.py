from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required
from init import db
from controllers.auth_controller import authorize
from models.item import Item, ItemSchema

items_bp = Blueprint('items', __name__, url_prefix='/items')


@items_bp.route('/')
@jwt_required()
def get_all_items():
    stmt = db.select(Item)
    items = db.session.scalars(stmt)
    return ItemSchema(many=True).dump(items)


@items_bp.route('/<int:id>')
def one_item(id):
    stmt = db.select(Item).filter_by(id=id)
    item = db.session.scalar(stmt)
    if item:
        return ItemSchema(many=False).dump(item)
    else:
        return {' ! ERROR ': f'NOT FOUND. Sorry, there\'s no item with ID {id}, please try another'}, 404

@items_bp.route("/new", methods=["POST"])
def create_new_item():
    
    # create a new item
    item = Item(
        brand=request.json["brand"],
        description=request.json["description"],
        department=request.json["department"],
        price=request.json["price"],
        store_id=request.json["store_id"],
        in_stock=request.json["in_stock"]
    )

    # Add created item to database
    db.session.add(item)
    db.session.commit()

    # response~
    return ItemSchema(many=False).dump(Item), 201

@items_bp.route('/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_one_item(id):
    authorize()

    stmt = db.select(Item).filter_by(id=id)
    item = db.session.scalar(stmt)
    if item:
        db.session.delete(item)
        db.session.commit()
        return {'message': f"Item '{item.description}' deleted successfully"}
    else:
        return {'error': f'Item not found with id {id}'}, 404