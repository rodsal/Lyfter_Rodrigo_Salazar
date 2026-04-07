from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Float, DateTime
from sqlalchemy import insert, select, update
import os
import bcrypt
from dotenv import load_dotenv

metadata_obj = MetaData()

user_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String(30)),
    Column("password", String),
    Column("role", String(20), default="user"),
)

product_table = Table(
    "products",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("price", Float),
    Column("enter_date", DateTime),
    Column("quantity", Integer),
)

invoice_table = Table(
    "invoices",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer),
    Column("product_id", Integer),
    Column("quantity_purchased", Integer),
    Column("purchase_date", DateTime),
    Column("total", Float),
)

load_dotenv()

class DB_Manager:
    def __init__(self):
        db_url = os.getenv('DATABASE_URL')
        self.engine = create_engine(db_url)
        metadata_obj.create_all(self.engine)
        from database.product import Product
        from database.invoice import Invoice
        self.products = Product(product_table, self.engine)
        self.invoices = Invoice(invoice_table, self.engine)
        
    def insert_user(self, username, password, role="user"):
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        stmt = insert(user_table).returning(user_table.c.id, user_table.c.role).values(username=username, password=hashed.decode(), role=role)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]

    def get_user(self, username):
        stmt = select(user_table).where(user_table.c.username == username)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()
            if len(users) == 0:
                return None
            return users[0]

    def get_user_by_id(self, id):
        stmt = select(user_table).where(user_table.c.id == id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()
            if len(users) == 0:
                return None
            return users[0]

    def purchase(self, user_id, product_id, new_quantity, quantity_purchased, purchase_date, total):
        update_stock = (
            update(product_table)
            .where(product_table.c.id == product_id)
            .values(quantity=new_quantity)
        )
        insert_invoice = insert(invoice_table).values(
            user_id=user_id,
            product_id=product_id,
            quantity_purchased=quantity_purchased,
            purchase_date=purchase_date,
            total=total,
        )
        with self.engine.begin() as conn:
            conn.execute(update_stock)
            conn.execute(insert_invoice)
