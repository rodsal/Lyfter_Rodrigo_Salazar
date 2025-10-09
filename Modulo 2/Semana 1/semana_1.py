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

def write_json_to_file(data_json, path):
    with open (path,'w') as json_file:
        json.dump(data_json,json_file, indent=4)


def status_validation(status):
    valid_statuses = ["Not Started", "In Progress", "Completed"]
    if status not in valid_statuses:
        raise ValueError("Status is not valid. Please use: Not Started, In Progress, or Completed.")

#CRUD
#Read

@app.route("/tasks/all")
def show_tasks():
    task_list = read_json_file(json_path)
    return {"data": task_list}

@app.route("/tasks")
def filtered_tasks():
    task_list = read_json_file(json_path)
    tasks_filtered = task_list
    status_filter = request.args.get("status")
    if status_filter:
        tasks_filtered = list(
            filter(lambda show: show["status"] == status_filter, tasks_filtered)
        )
    return {"data": tasks_filtered}

#Create

@app.route("/addtask", methods=["POST"])
def add_task():
    task_list = read_json_file(json_path)
    if not request.json:
        return jsonify(message = "No empty body allowed"), 400
    
    existing_ids = [task["ID"] for task in task_list]
    if request.json["ID"] in existing_ids:
        return jsonify(message="Task with this ID already exists"), 409

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
@app.route("/task/<task_id>", methods = ["PUT"])
def update_task(task_id):
    task_list = read_json_file(json_path)
    if not request.json:
        return jsonify(message = "No empty body allowed"), 400
    try:
        task_found = None
        for task in task_list:
            if task ["ID"] == task_id:
                task_found = task
                break
        
        if task_found == None:
            return jsonify(message="Task not found"), 404
        
        if "title" in request.json:
              task_found["title"] = request.json["title"]

        elif "description" in request.json:
              task_found["description"] = request.json["description"]
        elif "status" in request.json:
              status_validation(request.json["status"])
              task_found["status"] = request.json["status"]
        else:
            return jsonify(message="Json key not valid, please try with a valid key"),403
        write_json_to_file(task_list,json_path)
        return jsonify(message="Task updated successfully"), 200

    except ValueError as ex:
        return jsonify(message=str(ex)), 400    
    except Exception as ex:
        return jsonify(message=str(ex)), 500

#Delete
@app.route("/deletetask/<task_id>", methods = ["DELETE"])
def delete_task(task_id):
    task_list = read_json_file(json_path)
    try:
        task_found = None
        for task in task_list:
            if task["ID"] == task_id:
                task_found = task
                break
        
        if task_found is None:
            return jsonify(message="Task not found"), 404

        task_list.remove(task_found)
        write_json_to_file(task_list,json_path)
        return jsonify(message="Task deleted successfully", data=task_list), 200
    
    except Exception as ex:
         return jsonify(message=str(ex)), 500
    

if __name__ == "__main__":
    app.run(host="localhost",port="5040", debug=True)
