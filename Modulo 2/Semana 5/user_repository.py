class UserRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def _format_user(self, user_record):
        return {
            "id": user_record[0],
            "name": user_record[1],
            "email": user_record[2],
            "username": user_record[3],
            "birth_date": user_record[4],
            "state": user_record[5],
        }
    def _format_state(self, state_record):
        return {
            "state_id": state_record[0],
            "state": state_record[1],
        }

    def create_user(self, name, email, username, password, birth_date, state_id):
        try:
            self.db_manager.execute_query(
                "INSERT INTO users (name, email, username, password, birth_date, state_id) VALUES (%s, %s, %s, %s, %s, %s)",
                (name, email, username, password, birth_date, state_id),
            )
            print("User inserted successfully")
            return True
        except Exception as error:
            print("Error inserting a user into the database: ", error)
            return False

    def get_all_users(self):
        try:
            results = self.db_manager.execute_query(
                """
                SELECT 
                    users.id,
                    users.name, 
                    users.email, 
                    users.username, 
                    users.birth_date, 
                    user_states.state 
                FROM users 
                JOIN user_states ON users.state_id = user_states.id;
                """
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting all users from the database: ", error)
            return False

    def get_users_by_state(self, state):
        try:
            results = self.db_manager.execute_query(
                """
                SELECT 
                    users.id,
                    users.name, 
                    users.email, 
                    users.username, 
                    users.birth_date, 
                    user_states.state 
                FROM users 
                JOIN user_states ON users.state_id = user_states.id
                WHERE user_states.state = %s;
                """,
                (state,)
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting users by state from the database: ", error)
            return False
    
    def get_users_by_value(self, value,column_name):
        try:
            results = self.db_manager.execute_query(
                """
                SELECT 
                    users.id,
                    users.name, 
                    users.email, 
                    users.username, 
                    users.birth_date, 
                    user_states.state 
                FROM users 
                JOIN user_states ON users.state_id = user_states.id
                WHERE users."""+column_name+""" = %s;
                """,
                (value,)
            )
            formatted_results = [self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting users by "+column_name +" from the database: ", error)
            return False
    
    def get_valid_state(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT * FROM user_states;"
            )
            formatted_results = [self._format_state(result) for result in results]
            return formatted_results
        except Exception as error:
            print("Error getting valid state from the database: ", error)
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