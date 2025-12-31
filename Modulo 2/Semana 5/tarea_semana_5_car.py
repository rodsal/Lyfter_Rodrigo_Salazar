from flask import jsonify, Flask, request
from database_connection import PgManager
from flask.views import MethodView
from car_repository import CarRepository

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
        cars_repo = CarRepository(db_manager)
        formatted_results = getattr(cars_repo, option)(*args)
        return formatted_results


class Cars(MethodView):
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
                results = self.execution_query("get_cars_by_state", state)
            else:
                return jsonify(message="State not valid, please use " + self.print_available_list_DB("state")), 400

        car_model = request.args.get('model')
        if car_model:
            results = self.execution_query("get_cars_by_model", car_model)
            if len(results)>0:
                return jsonify({"data": results}), 200
            else:
                return jsonify(message="Car not found"), 400

        else:
            results = self.execution_query("get_all_cars")
        return jsonify({"data": results}), 200

    def post(self):
        if not request.json:
            return jsonify(message="No data provided"), 400

        valid_states = self.execution_query("get_valid_state")
        valid_states_list = [s['state'] for s in valid_states]
        valid_makes = self.execution_query("get_valid_make")
        valid_makes_list = [s['make'] for s in valid_makes]
        valid_models = self.execution_query("get_valid_model")
        valid_models_list = [(s['model'], s['model_year']) for s in valid_models]
        print(valid_models)
        #print(valid_models_list)

        state = request.json["state"]
        if state not in valid_states_list:
            return jsonify(message="State not valid, please use " + self.print_available_list_DB("state")), 400

        make = request.json["make"]
        if make not in valid_makes_list:
            return jsonify(message="Make not valid, please use " + self.print_available_list_DB("make")), 400

        model = request.json["model"]
        model_year = request.json["model_year"]
        print (model)
        print(model_year)
        if (model, model_year) not in valid_models_list:
            return jsonify(message="Model not valid, please use " + self.print_available_list_DB("model")), 400

        make_id = self.get_table_id(make, valid_makes, "make")
        model_id = self.get_model_id(model, model_year,valid_models)
        print(str(model_id))
        state_id = self.get_table_id(state, valid_states, "state")

        if not make_id or not model_id or not state_id:
            return jsonify(message="Missing required fields: make, model, state"), 400

        result = self.execution_query("create_car", make_id, model_id, state_id)
        print(result)
        if result:
            return jsonify(message="Car created successfully"), 201
        else:
            return jsonify(message="Error creating car"), 500

    def put(self, car_id):
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

        result = self.execution_query("update_car_state", car_id, state_id)

        if result:
            return jsonify(message="Car state updated successfully"), 200
        else:
            return jsonify(message="Error updating car state"), 500




cars_view = Cars.as_view('cars_api')
app.add_url_rule('/cars', methods=['GET', 'POST'], view_func=cars_view)
app.add_url_rule('/cars/<int:car_id>', methods=['PUT'], view_func=cars_view)


if __name__ == "__main__":
    app.run(host="localhost", port=5030, debug=True)

