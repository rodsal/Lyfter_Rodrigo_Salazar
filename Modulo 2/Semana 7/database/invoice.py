from sqlalchemy import insert, update, delete, select, func


class Invoice():
    def __init__(self, invoice_table, engine):
        self.invoice_table = invoice_table
        self.engine = engine

    def insert(self, user_id, quantity_purchased, product_id, purchase_date, total):
        add_invoice = insert(self.invoice_table).values(
            user_id=user_id, quantity_purchased=quantity_purchased, product_id=product_id,
            purchase_date=purchase_date, total=total
        )
        with self.engine.connect() as conn:
            result = conn.execute(add_invoice)
            conn.commit()
            return result

    def update(self, where_column, where_value, values_to_update):
        update_statement = (
            update(self.invoice_table)
            .where(self.invoice_table.c[where_column] == where_value)
            .values(**values_to_update)
        )
        with self.engine.connect() as conn:
            result = conn.execute(update_statement)
            conn.commit()
            return result

    def delete(self, where_column, where_value):
        delete_statement = delete(self.invoice_table).where(
            self.invoice_table.c[where_column] == where_value
        )
        with self.engine.connect() as conn:
            result = conn.execute(delete_statement)
            conn.commit()
            return result

    def get_by_user_id(self, user_id):
        stmt = select(self.invoice_table).where(self.invoice_table.c.user_id == user_id)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            return result.all()