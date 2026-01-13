from sqlalchemy import insert, update, delete, select, func

class User ():
    def __init__(self, user_table, engine, car_table=None):
        self.user_table = user_table
        self.engine = engine
        self.car_table = car_table

    def insert_user(self, name, full_name):
        add_user = insert(self.user_table).values(name= name, fullname=full_name)
        with self.engine.connect() as conn:
            result = conn.execute(add_user)
            conn.commit()
            return result

    def update_user(self, where_column, where_value, values_to_update):
        update_statement = (
            update(self.user_table)
            .where(self.user_table.c[where_column] == where_value)
            .values(**values_to_update)
        )
        with self.engine.connect() as conn:
            result = conn.execute(update_statement)
            conn.commit()
            return result
    
    def delete_user(self, where_column, where_value):
        delete_statement = delete(self.user_table).where(self.user_table.c[where_column] == where_value)

        with self.engine.connect() as conn:
            result = conn.execute(delete_statement)
            conn.commit()
            return result
       
    def select_users(self):
        statement = select(self.user_table)

        with self.engine.connect() as conn:
            result = conn.execute(statement)
            users = []
            for row in result:
                user_dict = {
                    "id": row.id,
                    "name": row.name,
                    "fullname": row.fullname
                }
                users.append(user_dict)
            return users
        

    def assign_more_than_1_car(self):

        if self.car_table is None:
            raise ValueError("car_table no está configurado. Pasa car_table al constructor de User.")

        stmt = (
            select(self.user_table.c.fullname)
            .select_from(self.car_table)
            .join(self.user_table, self.car_table.c.user_id == self.user_table.c.id)
            .group_by(self.user_table.c.fullname)
            .having(func.count(self.user_table.c.fullname) > 1)
        )

        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            users_with_multiple_cars = [row.fullname for row in result]
            return users_with_multiple_cars



