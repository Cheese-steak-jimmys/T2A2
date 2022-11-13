import os

from flask import Flask
# from flask_selfdoc import Autodoc
from marshmallow.exceptions import ValidationError

from controllers.auth_controller import auth_bp
from controllers.cli_controller import db_commands
from controllers.items_controller import items_bp
from controllers.orders_controller import orders_bp
from init import bcrypt, db, jwt, ma


def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(err):
        return {"ERROR": "Dear User, Your Request Was Not Found, Please Try Again"}, 404

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {"error": err.messages}, 400

    @app.errorhandler(400)
    def bad_request(err):
        return {"error": str(err)}, 400

    @app.errorhandler(401)
    def unauthorized(err):
        return {"error": "You are not authorized to perform this action"}, 401

    @app.errorhandler(KeyError)
    def key_error(err):
        return {"error": f"The field {err} is required."}, 400

    app.config["JSON_SORT_KEYS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(db_commands)
    app.register_blueprint(items_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(auth_bp)
    # app.register_blueprint(customers_bp)

    return app


# @app.route('/documentation')
# def documentation():
#     return auto.html()
