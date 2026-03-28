from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, Float
from sqlalchemy import insert, select
import os
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
    Column("enter_date", String(50)),
    Column("quantity", Integer),
)

invoice_table = Table(
    "invoices",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer),
    Column("product_id", Integer),
    Column("cantidad_comprada", Integer),
    Column("fecha_compra", String(50)),
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
        stmt = insert(user_table).returning(user_table.c.id, user_table.c.role).values(username=username, password=password, role=role)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result.all()[0]

    def get_user(self, username, password):
        stmt = select(user_table).where(user_table.c.username == username).where(user_table.c.password == password)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()

            if(len(users)==0):
                return None
            else:
                return users[0]

    def get_user_by_id(self, id):
        stmt = select(user_table).where(user_table.c.id == id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users = result.all()
            if(len(users)==0):
                return None
            else:
                return users[0]
