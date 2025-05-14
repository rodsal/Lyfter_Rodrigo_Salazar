import csv
import actions


def write_csv(path, data, headers):
  with open(path, 'w',encoding='utf-8') as file:
    write_into_file = csv.DictWriter(file, headers)
    write_into_file.writeheader()
    write_into_file.writerows(data)

def read_file(path):
    students = []
    with open(path, 'r', encoding='utf-8') as file:
        headers = file.readline().strip().split(',')
        for line in file:
            values = line.split(',')
            student = dict(zip(headers, values))
            students.append(student)
    return students

def request_import_file():
    import_file_path = input("Ingrese la ruta del archivo que desea importar: ")
    return import_file_path

def initialize_values():
   return True

