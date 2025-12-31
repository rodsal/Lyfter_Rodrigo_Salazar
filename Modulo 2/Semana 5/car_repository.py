class CarRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_car(self, car_record):
        return {
            "id": car_record[0],
            "make": car_record[1],
            "model": car_record[2],
            "model_year": car_record[3],
            "car_state": car_record[4]
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

    def create_car(self, make, model, state_id):
        try:
            self.db_manager.execute_query(
                "INSERT INTO car (make_id, model_id, state_id) VALUES (%s, %s, %s);",
                (make, model, state_id),
            )
            print("Car inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a car into the database: ", error)
            return False

    def get_all_cars(self):
        try:
            results = self.db_manager.execute_query(
                """
                SELECT car.id, make.make, model.model, model.model_year, car_state.state 
                FROM car 
                JOIN make ON car.make_id = make.id
                JOIN model ON car.model_id = model.id
                JOIN car_state ON car.state_id = car_state.id;
                """
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all car from the database: ", error)
            return False

    def get_cars_by_state(self, state):
        try:
            results = self.db_manager.execute_query(
                """
                SELECT car.id, make.make, model.model, model.model_year, car_state.state 
                FROM car 
                JOIN make ON car.make_id = make.id
                JOIN model ON car.model_id = model.id
                JOIN car_state ON car.state_id = car_state.id
                WHERE car_state.state = %s;
                """,
                (state,)
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting cars by state from the database: ", error)
            return False
    
    def get_cars_by_model(self, model):
        try:
            results = self.db_manager.execute_query(
                """
                SELECT car.id, make.make, model.model, model.model_year, car_state.state 
                FROM car 
                JOIN make ON car.make_id = make.id
                JOIN model ON car.model_id = model.id
                JOIN car_state ON car.state_id = car_state.id
                WHERE model.model = %s;
                """,
                (model,)
            )
            formatted_results = [self._format_car(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting cars by model from the database: ", error)
            return False
    
    def get_valid_state(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM car_state;"
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