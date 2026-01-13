from sqlalchemy import insert, update, delete, select

class Address ():
    def __init__(self, address_table, engine):
        self.address_table = address_table
        self.engine = engine

    def insert_address(self, user_id, email_address):
        add_address = insert(self.address_table).values(user_id= user_id, email_address=email_address)
        with self.engine.connect() as conn:
            result = conn.execute(add_address)
            conn.commit()
            return result

    def update_address(self, where_column, where_value, values_to_update):
        update_statement = (
            update(self.address_table)
            .where(self.address_table.c[where_column] == where_value)
            .values(**values_to_update)
        )
        with self.engine.connect() as conn:
            result = conn.execute(update_statement)
            conn.commit()
            return result
    
    def delete_address(self, where_column, where_value):
        delete_statement = delete(self.address_table).where(self.address_table.c[where_column] == where_value)

        with self.engine.connect() as conn:
            result = conn.execute(delete_statement)
            conn.commit()
            return result
        

    def select_addresses(self):
        statement = select(self.address_table)

        with self.engine.connect() as conn:
            result = conn.execute(statement)
            add = []
            for row in result:
                add_dict = {
                    "id": row.id,
                    "user_id": row.user_id,
                    "email_address": row.email_address
                }
                add.append(add_dict)
            return add
       
