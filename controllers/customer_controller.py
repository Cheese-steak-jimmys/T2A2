from flask import Blueprint, request 
from models.customer import Customer, CustomerSchema
from sqlalchemy.exc import IntegrityError
from init import db, bcrypt
customers_bp = Blueprint("customers", __name__, url_prefix="/customers")

@customers_bp.route('/auth/register/', methods=['POST'])
def auth_register():
    try:
        # create a new customer
        customer = Customer(
            name = request.json['name'],
            email = request.json['email'],
            address = request.json['address'],
            phone = request.json['phone'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf8'),
            membership = request.json['membership']
        )
            # Add customer to database
        db.session.add(customer)
        db.session.commit()

        # response
        return CustomerSchema(exclude=['password']).dump(Customer), 201
    except IntegrityError:
        return{'ERROR': 'The Email Or Phone Number Are Already In Use, Please Use Another'}, 409

# @app.route('/auth/register/', methods=['POST'])
# def auth_register():
#     try:
#         # create a new customer
#         customer = Customer(
#             email = request.json['email']
#             password = bcrypt.generate_password_hash(request.json['password']).decode('utf8'),
#             name = request.json['name']
#         )
#             # Add user to database
#         db.session.add(customer)
#         db.session.commit()

#         # response
#         return CustomerSchema(exclude=['password']).dump(Customer), 201
#     except IntegrityError:
#         return{'ERROR': 'This Email Is Already In Use'}, 409