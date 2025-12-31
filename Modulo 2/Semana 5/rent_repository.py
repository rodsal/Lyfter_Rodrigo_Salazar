class RentRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_rent(self, rent_record):
        return {
            "id": rent_record[0],
            "name": rent_record[1],
            "make": rent_record[2],
            "model": rent_record[3],
            "rent_date": rent_record[4],
            "rent_state": rent_record[5]
        }

    def _format_state(self, state_record):
        return {
            "state_id": state_record[0],
            "state": state_record[1],
        }
    
    def _format_make(self, make_record):
        return {
            "make_id": make_record[0],
            "make": make_record[1],
        }

    def _format_model(self, model_record):
        return {
            "model_id": model_record[0],
            "model": model_record[1],
            "model_year":model_record[2],
        }

    def create_rent(self, car, user, rent_date, rent_state):
        try:
            self.db_manager.execute_query(
                "INSERT INTO rent_car (car_id, user_id, rent_date, rent_state_id) VALUES (%s,%s,%s,%s);",
                (car, user, rent_date,rent_state),
            )
            print("Rent inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a rent into the database: ", error)
            return False

    def get_all_rents(self):
        try:
            results = self.db_manager.execute_query(
                """
                SELECT rent_car.id, users.name, make.make, model.model, rent_car.rent_date, rent_state.state
                FROM rent_car
                JOIN users ON rent_car.user_id = users.id
                JOIN car ON rent_car.car_id = car.id
                JOIN model ON car.model_id = model.id
                JOIN make ON car.make_id = make.id
                JOIN rent_state ON rent_car.rent_state_id = rent_state.id
                """
            )
            formatted_results = [self._format_rent(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all rents from the database: ", error)
            return False

    def get_rents_by_state(self, state):
        try:
            results = self.db_manager.execute_query(
                """
                SELECT rent_car.id, users.name, make.make, model.model, rent_car.rent_date, rent_state.state
                FROM rent_car
                JOIN users ON rent_car.user_id = users.id
                JOIN car ON rent_car.car_id = car.id
                JOIN model ON car.model_id = model.id
                JOIN make ON car.make_id = make.id
                JOIN rent_state ON rent_car.rent_state_id = rent_state.id
                WHERE rent_state.state = %s;
                """,
                (state,)
            )
            formatted_results = [self._format_rent(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting users by state from the database: ", error)
            return False
    
    
    def get_valid_state(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM rent_state;"
            )
            formatted_results = [self._format_state(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting valid state from the database: ", error)
            return False
        
    def get_valid_make(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM make;"
            )
            formatted_results = [self._format_make(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting valid makes from the database: ", error)
            return False

    def get_valid_model(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM model;"
            )
            formatted_results = [self._format_model(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting valid models from the database: ", error)
            return False

    def get_valid_car(self):
        try:
            results = self.db_manager.execute_query(
                """
                SELECT car.id, make.make, model.model, model.model_year
                FROM car
                JOIN make ON car.make_id = make.id
                JOIN model ON car.model_id = model.id;
                """
            )
            formatted_results = [{
                "car_id": result[0],
                "car": f"{result[1]} {result[2]} {result[3]}"
            } for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting valid cars from the database: ", error)
            return False

    def get_valid_user(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT id, name FROM users;"
            )
            formatted_results = [{
                "user_id": result[0],
                "user": result[1]
            } for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting valid users from the database: ", error)
            return False

    def get_car_id_by_rent(self, rent_id):
        try:
            results = self.db_manager.execute_query(
                "SELECT car_id FROM rent_car WHERE id = %s;",
                (rent_id,)
            )
            if results and len(results) > 0:
                return results[0][0]
            return None
        except Exception as error:
            print("Error getting car_id from rent: ", error)
            return None

    def update_rent_state(self, rent_id, state_id):
        try:
            self.db_manager.execute_query(
                "UPDATE rent_car SET rent_state_id = %s WHERE id = %s",
                (state_id, rent_id),
            )
            print("Rent state updated successfully")
            return True
        except Exception as error:
            print("Error updating rent state from the database: ", error)
            return False

    def update_car_state(self, car_id, state_id):
        try:
            self.db_manager.execute_query(
                "UPDATE car SET state_id = %s WHERE id = %s",
                (state_id, car_id),
            )
            print("Car state updated successfully")
            return True
        except Exception as error:
            print("Error updating car state from the database: ", error)
            return False

    def update_user(self, _id, name, email, username, birth_date, state_id):
        try:
            self.db_manager.execute_query(
                "UPDATE users SET (name, email, username, birth_date, state_id) = (%s, %s, %s, %s, %s) WHERE ID = %s",
                (name, email, username, birth_date, state_id, _id),
            )
            print("User updated successfully")
            return True
        except Exception as error:
            print("Error updating a user from the database: ", error)
            return False

    def delete_user(self, _id):
        try:
            self.db_manager.execute_query(
                "DELETE FROM users WHERE id = (%s)", (_id,)
            )
            print("User deleted successfully")
            return True
        except Exception as error:
            print("Error deleting a user from the database: ", error)
            return False