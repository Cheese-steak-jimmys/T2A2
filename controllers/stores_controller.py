from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from init import db
from models.store import Store, StoreSchema

stores_bp = Blueprint("stores", __name__, url_prefix="/stores")

# get all stores
@stores_bp.route("/")
@jwt_required()
def get_all_stores():
    stmt = db.select(Store)
    stores = db.session.scalars(stmt)
    return StoreSchema(many=True).dump(stores)

# get one store
@stores_bp.route("/<int:id>")
def one_store(id):
    stmt = db.select(Store).filter_by(id=id)
    store = db.session.scalar(stmt)
    # display chosen store
    if store:
        return StoreSchema(many=False).dump(store)
    else:
        return {
            " ! ERROR ": f"NOT FOUND. Sorry, there's no store with ID {id}, please try another"
        }, 404

 # create a new store
@stores_bp.route("/new", methods=["POST"])
def create_new_store():
    store = Store(
        suburb=request.json["suburb"],
        email=request.json["email"],
        phone=request.json["phone"]
    )
    # Add created store to database
    db.session.add(store)
    db.session.commit()

    # response~
    return StoreSchema(many=False).dump(store), 201
    # except IntegrityError:
    #     return {
    #         "ERROR": "Only An Admin Can Create A New Store"
    #     }, 409