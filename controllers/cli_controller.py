from datetime import date

from flask import Blueprint

from init import bcrypt, db
from models.customer import Customer
from models.item import Item
from models.order import Order
from models.store import Store

db_commands = Blueprint("db", __name__)


@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")


@db_commands.cli.command("seed")
def seed_db():
    customers = [
        Customer(
            name="P. Sherman",
            email="maleee@mail.com.au",
            address="42, wallaby way, sydney, 2000",
            password=bcrypt.generate_password_hash("indigo1").decode("utf-8"),
            is_member=True,
            acc_active=True
            # store_id= 1
        ),
        Customer(
            name="Johnny Ringo",
            address="12, pine Street, redcliff, 4000",
            email="baneofbris@mail.com",
            password=bcrypt.generate_password_hash("2468").decode("utf-8"),
            acc_active=True
            # store_id= 3
        ),
        Customer(
            email="harvesterofsorrow@tallica.com",
            address="1, eat street, hamilton, 4009",
            phone=555555552.3,
            password=bcrypt.generate_password_hash("foxtrot5").decode("utf-8"),
            acc_active=True
            # store_id= 1
        ),
        Customer(
            name="Vlad Midnight",
            email="vladtheinhaler@admin.com",
            address="1, eat street, hamilton, 4009",
            phone=44556622,
            password=bcrypt.generate_password_hash("foxtrot5").decode("utf-8"),
            is_member=True,
            is_admin=True,
            acc_active=True
            # store_id= 3
        ),
    ]

    db.session.add_all(customers)
    db.session.commit()

    stores = [
        Store(
            suburb="Kenmore", 
            email="stores.kenmore@mail.com.au"
            ),
        Store(
            suburb="Northlakes",
            email="stores.northlakes@mail.com.au"
             ),
        Store(
            suburb="Milton",
            email="stores.milton@mail.com.au"
            ),
    ]

    db.session.add_all(stores)
    db.session.commit()
    
    items = [
        Item(
            brand="arnotts's",
            description="monte carlo",
            department="grocery",
            price=2.55,
            in_stock=True,
        ),
        Item(
            brand="ACME mills",
            description="sourdough",
            department="bakery",
            price=4.10,
            in_stock=True,
        ),
        Item(
            brand="Java Java",
            description="iced espresso",
            department="perishables",
            price=2.40,
            in_stock=True,
            on_promotion=True,
        ),
    ]

    db.session.add_all(items)
    db.session.commit()

    orders = [
        Order(
            date=date.today(),
            customer_id=1,
            item_id=3,
            # item_id=2
        ),
        Order(
            date=date.today(),
            customer_id=2,
            # item_id = (),
        ),
        Order(
            date=date.today(),
            customer_id=3,
            # item_id = (),
        ),
    ]

    db.session.add_all(orders)
    db.session.commit()
    

    db.session.add_all(orders)
    db.session.add_all(items)
    db.session.add_all(customers)
    db.session.add_all(stores)
    db.session.commit()

    print("Tables seeded")
