from flask import Blueprint

from init import db
from models.store import Store, StoreSchema

stores_bp = Blueprint("stores", __name__, url_prefix="/stores")


@stores_bp.route("/")
# @jwt_required()
def get_all_stores():
    stmt = db.select(Store)
    stores = db.session.scalars(stmt)
    return StoreSchema(many=True).dump(stores)


@stores_bp.route("/<int:id>")
def one_item(id):
    stmt = db.select(Store).filter_by(id=id)
    store = db.session.scalar(stmt)
    if store:
        return StoreSchema(many=False).dump(store)
    else:
        return {
            " ! ERROR ": f"NOT FOUND. Sorry, there's no store with ID {id}, please try another"
        }, 404
