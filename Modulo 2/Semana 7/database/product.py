from sqlalchemy import insert, update, delete, select, func


class Product():
    def __init__(self, product_table, engine):
        self.product_table = product_table
        self.engine = engine

    def insert(self, name, price, quantity, enter_date):
        add_product = insert(self.product_table).values(
            name=name, price=price, quantity=quantity, enter_date=enter_date
        )
        with self.engine.connect() as conn:
            result = conn.execute(add_product)
            conn.commit()
            return result

    def update(self, where_column, where_value, values_to_update):
        update_statement = (
            update(self.product_table)
            .where(self.product_table.c[where_column] == where_value)
            .values(**values_to_update)
        )
        with self.engine.connect() as conn:
            result = conn.execute(update_statement)
            conn.commit()
            return result

    def delete(self, where_column, where_value):
        delete_statement = delete(self.product_table).where(
            self.product_table.c[where_column] == where_value
        )
        with self.engine.connect() as conn:
            result = conn.execute(delete_statement)
            conn.commit()
            return result

    def get_all(self):
        stmt = select(self.product_table)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            return result.all()

    def get_by_id(self, product_id):
        stmt = select(self.product_table).where(self.product_table.c.id == product_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            products = result.all()
            if len(products) == 0:
                return None
            return products[0]