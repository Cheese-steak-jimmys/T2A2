from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from init import db, ma
from controllers.items_controller import items_bp
from controllers.orders_controller import orders_bp
# from controllers.cli_controller import db_commands
# from init import bcrypt, db, jwt, ma


def create_app():
    app = Flask(__name__)

    # app.config["JSON_SORT_KEYS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    # app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    # bcrypt.init_app(app)
    # jwt.init_app(app)

    # app.register_blueprint(db_commands)
    app.register_blueprint(items_bp)
    app.register_blueprint(orders_bp)

    return app
