from sqlalchemy import insert, update, delete, select

class Car ():
    def __init__(self, car_table, engine):
        self.car_table = car_table
        self.engine = engine

    def insert_car(self, user_id,make,model,year,license_plate,color):
        add_car = insert(self.car_table).values(user_id = user_id, make = make ,model = model, year = year,license_plate = license_plate, color=color)
        with self.engine.connect() as conn:
            result = conn.execute(add_car)
            conn.commit()
            return result
    
    def insert_car_without_user(self,make,model,year,license_plate,color):
        add_car = insert(self.car_table).values(make = make ,model = model, year = year,license_plate = license_plate, color=color)
        with self.engine.connect() as conn:
            result = conn.execute(add_car)
            conn.commit()
            return result

    def update_car(self, where_column, where_value, values_to_update):
        update_statement = (
            update(self.car_table)
            .where(self.car_table.c[where_column] == where_value)
            .values(**values_to_update)
        )
        with self.engine.connect() as conn:
            result = conn.execute(update_statement)
            conn.commit()
            return result
    
    def delete_car(self, where_column, where_value):
        delete_statement = delete(self.car_table).where(self.car_table.c[where_column] == where_value)

        with self.engine.connect() as conn:
            result = conn.execute(delete_statement)
            conn.commit()
            return result
       

    def assign_user_to_car(self, user_id, license_plate):
        update_statement = (
            update(self.car_table)
            .where(self.car_table.c.license_plate == license_plate)
            .values(user_id=user_id)
        )
        with self.engine.connect() as conn:
            result = conn.execute(update_statement)
            conn.commit()
            return result
        
    def select_cars(self):
        statement = select(self.car_table)

        with self.engine.connect() as conn:
            result = conn.execute(statement)
            cars = []
            for row in result:
                car_dict = {
                    "id": row.id,
                    "user_id": row.user_id,
                    "make": row.make,
                    "model": row.model,
                    "year": row.year,
                    "license_plate": row.license_plate,
                    "color": row.color
                }
                cars.append(car_dict)
            return cars
        


    def select_cars_without_user(self):
        statement = select(self.car_table).where(self.car_table.c.user_id.is_(None))
        with self.engine.connect() as conn:
            result = conn.execute(statement)
            cars = []
            for row in result:
                car_dict = {
                    "id": row.id,
                    "user_id": row.user_id,
                    "make": row.make,
                    "model": row.model,
                    "year": row.year,
                    "license_plate": row.license_plate,
                    "color": row.color
                }
                cars.append(car_dict)
            return cars



