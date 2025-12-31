from flask import jsonify, Flask, request
from database_connection import PgManager
from flask.views import MethodView
from user_repository import UserRepository

app = Flask(__name__)


class Database:
    @staticmethod
    def call_query(option, *args):
        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="Rods@l01",
        host="localhost"
        )
        users_repo = UserRepository(db_manager)
        formatted_results = getattr(users_repo, option)(*args)
        return formatted_results

        #print(formatted_results


class Users(MethodView):
    def execution_query(self, query_name, *args):
        db = Database()
        results = db.call_query(query_name, *args)
        return results
    
    def state_validation (self, valid_states_list,input_state):
        for state in valid_states_list:
            if state == input_state:
                return True
        return False
    
    def get_state_id (self,input_state, valid_states):      
        for state in valid_states:
            if state.get('state') == input_state:
                return state.get('state_id')
                break
    
    def print_available_states(self):
        print("Available states:")
        valid_states = self.execution_query("get_valid_state")
        states_string = ""
        for state in valid_states:
            states_string = states_string + state.get('state') + ", "
        return states_string

            
    def get(self):
        valid_state = self.execution_query("get_valid_state")
        state = request.args.get('state')
        value_search = ['id', 'name', 'email', 'username']
        if state:
            valid_states_list = [s['state'] for s in valid_state]
            if state in valid_states_list:
                results = self.execution_query("get_users_by_state", state)
            else:
                return jsonify(message="State not valid, please use " + self.print_available_states()), 400
        for column in value_search:
            requested_value = request.args.get(column)
            if requested_value:
                results = self.execution_query("get_users_by_value", requested_value,column)
                if len(results)>0:
                    break
                else:
                    return jsonify(message="Users not found"), 404
        else:
            results = self.execution_query("get_all_users")
        return jsonify({"data": results}), 200

    def post(self):
        if not request.json:
            return jsonify(message="No empty body allowed"), 400
        try:
            valid_states = self.execution_query("get_valid_state")
            valid_states_list = [s['state'] for s in valid_states]
            required_fields = ["name", "email", "username", "password", "birth_date", "state"]
            missing_fields = [field for field in required_fields if field not in request.json]
            if missing_fields:
                return jsonify(message=f"Missing fields: {', '.join(missing_fields)}"), 400
            state = request.json["state"]
            if state not in valid_states_list:
                return jsonify(message="State not valid, please use " + self.print_available_states()), 400
            name = request.json["name"]
            email =  request.json["email"]
            username = request.json["username"]
            password = request.json["password"]
            birth_date =  request.json["birth_date"]
            state_id = self.get_state_id(state, valid_states)
            result = self.execution_query("create_user",name, email,username,password,birth_date,state_id)
            if result:
                return jsonify(message="User added successfully"), 201
            else:
                return jsonify(message="Failed to create user"), 409
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify(message=str(ex)), 500


    def put(self, user_id):
        if not request.json:
            return jsonify(message="No empty body allowed"), 400
        try:
            user = self.execution_query("get_users_by_value", user_id,"id")
            if len(user) < 0:
                return jsonify(message="User not found"),404
            if "name" in request.json:
                name = request.json["name"]
            else:
                name = user[0]["name"]
            if "email" in request.json:
                email = request.json["email"]
            else:
                email = user[0]["email"]
            if "username" in request.json:
                username = request.json["username"]
            else:
                username = user[0]["username"]
            if "bith_date" in request.json:
                birth_date = request.json["birth_date"]
            else:
                birth_date = user[0]["birth_date"]
            valid_states = self.execution_query("get_valid_state")
            if "state" in request.json:
                valid_states = self.execution_query("get_valid_state")
                valid_states_list = [s['state'] for s in valid_states]
                state = request.json["state"]

                if not self.state_validation(valid_states_list, state):
                    return jsonify(message="State not valid, please use " + self.print_available_states()), 400
                state_id = self.get_state_id(state,valid_states)
                print(state_id)
            else:
                print("else")
                state = user[0]["state"]
                print(state)
                state_id = self.get_state_id(state,valid_states)
                print(state_id)
            #if not any(key in request.json for key in ["title", "description", "status"]):
            #    return jsonify(message="Json key not valid, please try with a valid key"), 400
            success_query = self.execution_query("update_user", user_id,name,email, username, birth_date, state_id)
            if success_query:
                return jsonify(message="User updated successfully"), 200
            else:
                return jsonify(message="Failed to update user"), 409
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify(message=str(ex)), 500


    def delete(self, user_id):
        try:
            user = self.execution_query("get_users_by_value", user_id,"id")
            print(user)
            if not user:
                return jsonify(message="User not found"),404
            self.execution_query("delete_user", user_id)
            return jsonify(message="Task deleted successfully", data=user), 200
        except Exception as ex:
            return jsonify(message=str(ex)), 500

users_view = Users.as_view('users_api')
app.add_url_rule('/users', methods=['GET', 'POST'], view_func=users_view)
app.add_url_rule('/users/<user_id>', methods=['PUT', 'DELETE'], view_func=users_view)


if __name__ == "__main__":
    app.run(host="localhost", port=5030, debug=True)

