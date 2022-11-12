from flask import Blueprint
from datetime import date
from models.customer import Customer
from models.order import Order
from models.item import Item
from init import db, bcrypt

db_commands = Blueprint("db", __name__)


@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_db():
    customers = [
        Customer(
            email='male@mail.com.au',
            address='42, wallaby way, sydney, 2000',
            password=bcrypt.generate_password_hash('indigo1').decode('utf-8'),
            is_member=True
        ),
        Customer(
            name='Johnny Ringo',
            address='12, pine Street, redcliff, 4000',
            email='baneofbris@mail.com',
            password=bcrypt.generate_password_hash('2468').decode('utf-8')
        ),
        Customer(
            email='harvesterofsorrow@tallica.com',
            address='1, eat street, hamilton, 4009',
            phone=5555555523,
            password=bcrypt.generate_password_hash('foxtrot5').decode('utf-8')
        )
    ]

    db.session.add_all(customers)
    db.session.commit()

    items = [
        Item(
            brand = 'arnotts\'s',
            description = 'monte carlo',
            department = 'grocery',
            price =2,
            in_stock = True
        ),
        Item(
            brand = 'ACME mills',
            description = 'sourdough',
            department = 'bakery',
            price =4,
            in_stock = True
        ),
        Item(
            brand = 'Java Java',
            description = 'iced espresso',
            department = 'perishables',
            price =4,
            in_stock = True,
            on_promotion = True
        )
    ]

    db.session.add_all(items)
    db.session.commit()

    orders = [
        Order(
            date = date.today,
            customer_id = 1,
            item_id = 0,
            total_amount = 5
        ),
        Order(
            date = date.today,
            customer_id = 2,
            item_id = 2,
            total_amount = 3
        ),
        Order(
            date = date.today,
            customer_id = 0,
            item_id = 1,
            total_amount = 6
        )
    ]

    db.session.add_all(orders)
    db.session.add_all(items)
    db.session.add_all(customers)
    db.session.commit()

    print('Tables seeded')