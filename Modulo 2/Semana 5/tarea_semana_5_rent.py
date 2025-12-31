from flask import jsonify, Flask, request
from database_connection import PgManager
from flask.views import MethodView
from rent_repository import RentRepository

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
        rents_repo = RentRepository(db_manager)
        formatted_results = getattr(rents_repo, option)(*args)
        return formatted_results

    


class Rents(MethodView):
    def execution_query(self, query_name, *args):
        db = Database()
        results = db.call_query(query_name, *args)
        return results
    
    def print_available_list_DB(self, table):
        valid_columns = self.execution_query("get_valid_"+str(table)+"")
        join_string = ""
        for state in valid_columns:
            join_string = join_string + state.get(str(table)) + ", "
        return join_string       
    
    def value_validation (self, valid_list,input_value):
        for state in valid_list:
            if state == input_value:
                return True
        return False
    
    def get_table_id (self,input_value, valid_list, table):      
        for state in valid_list:
            if state.get(str(table)) == input_value:
                return state.get(''+ str(table)+'_id')
            
    def get_model_id (self,input_model, input_year,valid_list):      
        for model in valid_list:
            print(f'Model {input_model}, model array {model.get('model')}, Year {input_year}, year array {model.get('model_year')}')
            if model.get('model') == input_model and model.get('model_year') == input_year:
                return model.get('model_id')

            
    def get(self):
        valid_state = self.execution_query("get_valid_state")
        state = request.args.get('state')
        if state:
            valid_states_list = [s['state'] for s in valid_state]
            if state in valid_states_list:
                results = self.execution_query("get_rents_by_state", state)
            else:
                return jsonify(message="State not valid, please use " + self.print_available_list_DB("state")), 400

        else:
            results = self.execution_query("get_all_rents")
        return jsonify({"data": results}), 200

    def post(self):
        if not request.json:
            return jsonify(message="No data provided"), 400

        valid_cars = self.execution_query("get_valid_car")
        valid_cars_list = [c['car'] for c in valid_cars]
        valid_users = self.execution_query("get_valid_user")
        valid_users_list = [u['user'] for u in valid_users]
        valid_states = self.execution_query("get_valid_state")
        valid_states_list = [s['state'] for s in valid_states]

        car = request.json.get("car")
        if not car or car not in valid_cars_list:
            return jsonify(message="Car not valid, available cars: " + ", ".join(valid_cars_list)), 400

        user = request.json.get("user")
        if not user or user not in valid_users_list:
            return jsonify(message="User not valid, available users: " + ", ".join(valid_users_list)), 400

        state = request.json.get("state")
        if not state or state not in valid_states_list:
            return jsonify(message="State not valid, please use " + self.print_available_list_DB("state")), 400

        rent_date = request.json.get("rent_date")
        if not rent_date:
            return jsonify(message="Missing required field: rent_date"), 400

        car_id = self.get_table_id(car, valid_cars, "car")
        user_id = self.get_table_id(user, valid_users, "user")
        state_id = self.get_table_id(state, valid_states, "state")

        if not car_id or not user_id or not state_id:
            return jsonify(message="Missing required fields: car, user, state, rent_date"), 400

        result = self.execution_query("create_rent", car_id, user_id, rent_date, state_id)

        if result:
            return jsonify(message="Rent created successfully"), 201
        else:
            return jsonify(message="Error creating rent"), 500

    def put(self, rents_id):
        data = request.get_json()

        if not data:
            return jsonify(message="No data provided"), 400

        state = data.get('state')

        if not state:
            return jsonify(message="Missing required field: state"), 400

        valid_states = self.execution_query("get_valid_state")
        valid_states_list = [s['state'] for s in valid_states]

        if state not in valid_states_list:
            return jsonify(message="State not valid, please use " + self.print_available_list_DB("state")), 400

        state_id = self.get_table_id(state, valid_states, "state")

        result = self.execution_query("update_rent_state", rents_id, state_id)

        if result:
            if state.lower() == "completed":
                car_id = self.execution_query("get_car_id_by_rent", rents_id)
                if car_id:
                    from car_repository import CarRepository
                    from database_connection import PgManager

                    db_manager = PgManager(
                        db_name="postgres",
                        user="postgres",
                        password="Rods@l01",
                        host="localhost"
                    )
                    car_repo = CarRepository(db_manager)
                    car_states = car_repo.get_valid_state()
                    available_state_id = None
                    for s in car_states:
                        if s['state'].lower() == "available":
                            available_state_id = s['state_id']
                            break

                    if available_state_id:
                        car_repo.update_car_state(car_id, available_state_id)
                        return jsonify(message="Rent completed successfully and car is now available"), 200

            return jsonify(message="Rent state updated successfully"), 200
        else:
            return jsonify(message="Error updating rent state"), 500



rents_view = Rents.as_view('rents_api')
app.add_url_rule('/rents', methods=['GET', 'POST'], view_func=rents_view)
app.add_url_rule('/rents/<int:rents_id>', methods=['PUT'], view_func=rents_view)


if __name__ == "__main__":
    app.run(host="localhost", port=5030, debug=True)

