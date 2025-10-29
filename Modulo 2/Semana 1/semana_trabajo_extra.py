
from flask import Flask, request, jsonify
import json
from flask.views import MethodView
import uuid

app = Flask(__name__)
json_path = "data_consistency.json"
users_path = "users.json"

class Utils:

    @staticmethod
    def read_json_file(path):
        try:
            with open(path, 'r') as json_to_read:
                data_json = json.load(json_to_read)
            return data_json
        except FileNotFoundError:
            print("El archivo no existe. Se creará uno nuevo con una lista vacía.")
            Utils.write_json_to_file([], path)
            return []
        except json.JSONDecodeError:
            print("El archivo está vacío o contiene un JSON inválido.")
            return []
        raise

    @staticmethod
    def write_json_to_file(data_json, path):
        with open(path, 'w') as json_file:
            json.dump(data_json, json_file, indent=4)

class User_Login(MethodView):
    def save_token(self, json_data, email, token):
        for user in json_data:
            if user["email"] == email:
                user["token"] = token
        Utils.write_json_to_file(json_data, users_path)

    def post(self):
        if not request.json:
            return jsonify(message="No empty body allowed"), 400
        data = request.json
        if not data or "email" not in data or "password" not in data:
            return jsonify(message="Email and password required"), 400
        users = Utils.read_json_file(users_path)
        for user in users:
            if user["email"] == data["email"] and user["password"] == data["password"]:
                if "token" in user and user["token"]:
                    return jsonify(message="Login successful", token=user["token"]), 200
                token = str(uuid.uuid4())
                self.save_token(users, data["email"], token)
                return jsonify(message="Login successful", token=token), 200
        return jsonify(message="Invalid credentials"), 401

class Logout(MethodView):
    def post(self):
        token_provided = request.headers.get("token", "")
        users = Utils.read_json_file(users_path)
        for user in users:
            if user.get("token") == token_provided:
                user["token"] = ""
                Utils.write_json_to_file(users, users_path)
                return jsonify(message="Logout successful"), 200
        return jsonify(message="Invalid token"), 401

class Tasks(MethodView):

    def status_validation(self, status):
        valid_statuses = ["Not Started", "In Progress", "Completed"]
        if status not in valid_statuses:
            raise ValueError("Status is not valid. Please use: Not Started, In Progress, or Completed.")

    def validate_token(self, json_users, token_provided):
        for user in json_users:
            if user.get("token") == token_provided:
                return
        return jsonify(message="Token provided is not valid"), 401

    def get(self):
        token_provided = request.headers.get("token", "")
        json_users = Utils.read_json_file(users_path)
        validation_result = self.validate_token(json_users, token_provided)
        if validation_result:
            return validation_result
        task_list = Utils.read_json_file(json_path)
        status_filter = request.args.get("status")
        if status_filter:
            tasks_filtered = list(filter(lambda show: show["status"] == status_filter, task_list))
            return {"data": tasks_filtered}
        else:
            return {"data": task_list}

    def post(self):
        token_provided = request.headers.get("token", "")
        json_users = Utils.read_json_file(users_path)
        validation_result = self.validate_token(json_users, token_provided)
        if validation_result:
            return validation_result
        task_list = Utils.read_json_file(json_path)
        if not request.json:
            return jsonify(message="No empty body allowed"), 400
        existing_ids = [task["ID"] for task in task_list]
        if request.json["ID"] in existing_ids:
            return jsonify(message="Task with this ID already exists"), 409
        try:
            required_fields = ["ID", "title", "description", "status"]
            missing_fields = [field for field in required_fields if field not in request.json]
            if missing_fields:
                return jsonify(message=f"Missing fields: {', '.join(missing_fields)}"), 400
            self.status_validation(request.json["status"])
            task_to_add = {
                "ID": request.json["ID"],
                "title": request.json["title"],
                "description": request.json["description"],
                "status": request.json["status"],
            }
            task_list.append(task_to_add)
            Utils.write_json_to_file(task_list, json_path)
            return jsonify(message="Task added successfully", data=task_to_add), 201
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify(message=str(ex)), 500

    def put(self, task_id):
        token_provided = request.headers.get("token", "")
        json_users = Utils.read_json_file(users_path)
        validation_result = self.validate_token(json_users, token_provided)
        if validation_result:
            return validation_result
        task_list = Utils.read_json_file(json_path)
        if not request.json:
            return jsonify(message="No empty body allowed"), 400
        try:
            task_found = None
            for task in task_list:
                if task["ID"] == task_id:
                    task_found = task
                    break
            if task_found is None:
                return jsonify(message="Task not found"), 404
            if "title" in request.json:
                task_found["title"] = request.json["title"]
            if "description" in request.json:
                task_found["description"] = request.json["description"]
            if "status" in request.json:
                self.status_validation(request.json["status"])
                task_found["status"] = request.json["status"]
            if not any(key in request.json for key in ["title", "description", "status"]):
                return jsonify(message="Json key not valid, please try with a valid key"), 400
            Utils.write_json_to_file(task_list, json_path)
            return jsonify(message="Task updated successfully"), 200
        except ValueError as ex:
            return jsonify(message=str(ex)), 400
        except Exception as ex:
            return jsonify(message=str(ex)), 500

    def delete(self, task_id):
        token_provided = request.headers.get("token", "")
        json_users = Utils.read_json_file(users_path)
        validation_result = self.validate_token(json_users, token_provided)
        if validation_result:
            return validation_result
        task_list = Utils.read_json_file(json_path)
        try:
            task_found = None
            for task in task_list:
                if task["ID"] == task_id:
                    task_found = task
                    break
            if task_found is None:
                return jsonify(message="Task not found"), 404
            task_list.remove(task_found)
            Utils.write_json_to_file(task_list, json_path)
            return jsonify(message="Task deleted successfully", data=task_list), 200
        except Exception as ex:
            return jsonify(message=str(ex)), 500

tasks_view = Tasks.as_view('task_api')
app.add_url_rule('/task', methods=['GET', 'POST'], view_func=tasks_view)
app.add_url_rule('/task/<task_id>', methods=['PUT', 'DELETE'], view_func=tasks_view)
app.add_url_rule('/login', methods=['POST'], view_func=User_Login.as_view('login_api'))
app.add_url_rule('/logout', methods=['POST'], view_func=Logout.as_view('logout_api'))

if __name__ == "__main__":
    app.run(host="localhost", port=5030, debug=True)
