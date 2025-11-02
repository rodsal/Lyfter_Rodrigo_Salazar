#crear un modulo, para validar si el body esta vacío

from flask import Flask, request, jsonify
import json

app = Flask(__name__)
json_path="data_consistency.json"

def read_json_file(path):
    try:
        with open(path, 'r') as json_to_read:
            data_json = json.load(json_to_read)  
        return data_json
    except json.JSONDecodeError:
        print("El archivo está vacío o contiene un JSON inválido.")
        raise

def read_json_file(path):
    try:
        with open(path, 'r') as json_to_read:
            data_json = json.load(json_to_read)
        return data_json
    except FileNotFoundError:
        print("El archivo no existe. Se creará uno nuevo con una lista vacía.")
        write_json_to_file([],json_path)
    except json.JSONDecodeError:
        print("El archivo está vacío o contiene un JSON inválido.")
        raise


def write_json_to_file(data_json, path):
    with open (path,'w') as json_file:
        json.dump(data_json,json_file, indent=4)


def status_validation(status):
    valid_statuses = ["Not Started", "In Progress", "Completed"]
    if status not in valid_statuses:
        raise ValueError("Status is not valid. Please use: Not Started, In Progress, or Completed.")
    
def find_task (task_id, task_list):
    task_found = None
    for task in task_list:
            if task ["ID"] == task_id:
                task_found = task
                return task_found
                

#CRUD
#Read

@app.route("/tasks")
def show_tasks():
    task_list = read_json_file(json_path)
    return jsonify({"data": task_list})

@app.route("/tasks")
def filtered_tasks():
    task_list = read_json_file(json_path)
    tasks_filtered = task_list
    status_filter = request.args.get("status")
    if status_filter:
        tasks_filtered = list(
            filter(lambda show: show["status"] == status_filter, tasks_filtered)
        )
    return jsonify({"data": tasks_filtered})

@app.route("/tasks/<task_id>")
def show_task_by_id(task_id):
    task_list = read_json_file(json_path)
    try:
        task_found = find_task(task_id, task_list)

        if task_found == None:
            return jsonify(message="Task not found"), 404 
        
        return jsonify({"data": task_found}), 200

    except Exception as ex:
        return jsonify(message=str(ex)), 500

#Create

@app.route("/tasks", methods=["POST"])
def add_task():
    task_list = read_json_file(json_path)
    if not request.json:
        return jsonify(message = "No empty body allowed"), 400

    try:
        if "ID" not in request.json:
              raise ValueError ("ID is not on the request body")
        if "title" not in request.json:
              raise ValueError ("title is not on the request body")
        if "description" not in request.json:
              raise ValueError ("description is not on the request body")
        if "status" not in request.json:
              raise ValueError ("status not in the request body")
        else:
            status_validation(request.json["status"])

        existing_ids = [task["ID"] for task in task_list]
        if request.json["ID"] in existing_ids:
            return jsonify(message="Task with this ID already exists"), 409
        
        task_to_add= {
                "ID": request.json["ID"],
                "title": request.json["title"],
                "description": request.json["description"],
                "status": request.json["status"],
            }
        task_list.append(task_to_add)
        write_json_to_file(task_list,json_path)
        return jsonify(message="Task added successfully", data=task_to_add), 201
         
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 500


#Update
@app.route("/tasks/<task_id>", methods = ["PUT"])
def update_task(task_id):
    task_list = read_json_file(json_path)
    if not request.json:
        return jsonify(message = "No empty body allowed"), 400
    try:
        task_found = find_task(task_id, task_list)

        if task_found == None:
            return jsonify(message="Task not found"), 404 
        
        mandatory_keys = ["title", "description", "status"]

        for key in mandatory_keys:
            print (request.json)
            print(key)
            key_not_found = False
            if key in request.json:
                task_found[key] = request.json[key]
            else:
                key_found = True
        if key_not_found:
            return jsonify(message="Json key not valid, please try with a valid key"),400
        
        write_json_to_file(task_list,json_path)
        return jsonify(message="Task updated successfully"), 200

    except ValueError as ex:
        return jsonify(message=str(ex)), 400    
    except Exception as ex:
        return jsonify(message=str(ex)), 500

#Delete
@app.route("/tasks/<task_id>", methods = ["DELETE"])
def delete_task(task_id):
    task_list = read_json_file(json_path)
    try:
        task_found = find_task(task_id, task_list)
        
        if task_found is None:
            return jsonify(message="Task not found"), 404

        task_list.remove(task_found)
        write_json_to_file(task_list,json_path)
        return jsonify(message="Task deleted successfully", data=task_list), 200
    
    except Exception as ex:
         return jsonify(message=str(ex)), 500
    

if __name__ == "__main__":
    app.run(host="localhost",port="5040", debug=True)
