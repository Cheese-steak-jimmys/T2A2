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
            phone='5555555523',
            password=bcrypt.generate_password_hash('foxtrot5').decode('utf-8')
        )
    ]

    db.session.add_all(customers)
    db.session.commit()

    items = [
        Card(
            title = 'Start the project',
            description = 'Stage 1 - Create the database',
            status = 'To Do',
            priority = 'High',
            date = date.today(),
            user = users[0]
        ),
        Card(
            title = "SQLAlchemy",
            description = "Stage 2 - Integrate ORM",
            status = "Ongoing",
            priority = "High",
            date = date.today(),
            user = users[0]
        ),
        Card(
            title = "ORM Queries",
            description = "Stage 3 - Implement several queries",
            status = "Ongoing",
            priority = "Medium",
            date = date.today(),
            user = users[1]
        ),
        Card(
            title = "Marshmallow",
            description = "Stage 4 - Implement Marshmallow to jsonify models",
            status = "Ongoing",
            priority = "Medium",
            date = date.today(),
            user = users[1]
        )
    ]

    db.session.add_all(items)
    db.session.commit()

    comments = [
        Comment(
            message = 'Comment 1',
            user = users[1],
            card = cards[0],
            date = date.today()
        ),
        Comment(
            message = 'Comment 2',
            user = users[0],
            card = cards[0],
            date = date.today()
        ),
        Comment(
            message = 'Comment 3',
            user = users[0],
            card = cards[2],
            date = date.today()
        )
    ]

    db.session.add_all(comments)
    db.session.commit()

    print('Tables seeded')