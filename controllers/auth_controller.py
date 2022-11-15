from flask import Blueprint, request, abort
from init import db, bcrypt
from datetime import timedelta
from models.customer import Customer, CustomerSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/customers")
def get_customers():
    stmt = db.select(Customer)
    customers = db.session.scalars(stmt)
    return CustomerSchema(exclude=["password"]).dump(customers)


@auth_bp.route("/register", methods=["POST"])
def auth_register():
    try:
        # create a new customer
        customer = Customer(
            name=request.json["name"],
            email=request.json["email"],
            address=request.json["address"],
            phone=request.json["phone"],
            password=bcrypt.generate_password_hash(request.json["password"]).decode(
                "utf8"
            ),
        )
        # Add customer to database
        db.session.add(customer)
        db.session.commit()

        # response~
        return CustomerSchema(exclude=["password"]).dump(Customer), 201
    except IntegrityError:
        return {
            "ERROR": "The Email Or Phone Number Are Already In Use, Please Use Another"
        }, 409


@auth_bp.route("/login", methods=["POST"])
def auth_login():
    # Find a user by email address
    stmt = db.select(Customer).filter_by(email=request.json["email"])
    customer = db.session.scalar(stmt)
    # If user exists and password is correct
    if customer and bcrypt.check_password_hash(
        customer.password, request.json["password"]
    ):
        # return UserSchema(exclude=['password']).dump(user)
        token = create_access_token(
            identity=str(customer.id), expires_delta=timedelta(days=1)
        )
        return {"email": customer.email, "token": token, "is_admin": customer.is_admin}
    else:
        return {"ERROR": "Invalid email or password"}, 401


# def authorize():
#     customer_id = get_jwt_identity()
#     stmt = db.select(Customer).filter_by(id=customer_id)
#     customer = db.session.scalar(stmt)
#     if not customer.is_admin:
#         abort(401)
