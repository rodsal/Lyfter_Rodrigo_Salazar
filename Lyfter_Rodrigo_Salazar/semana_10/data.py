import json
import csv

def add_to_json_format(name,section,spanish_grade,english_grade,ss_grade,science_grade):
    add_student = {
        "nombre_completo": name,
        "section": section,
        "grades":
            {
            "nota_español": spanish_grade,
            "nota_ingles": english_grade,
            "social_studies_grade": ss_grade,
            "nota_ciencias": science_grade
            }     
    }
    return add_student


def write_json_to_file(students, path):
    with open (path,'w') as students_to_file:
        json.dump(students,students_to_file, indent=4)

def read_student_info(path):
    try:
        with open(path, 'r') as json_to_read:
            student_json = json.load(json_to_read)  
        return student_json
    except json.JSONDecodeError as exception:
        print("El archivo está vacío o contiene un JSON inválido. Agregue un estudiante para continuar")
        

def write_csv(path, data, headers):
  with open(path, 'w',encoding='utf-8') as file:
    write_into_file = csv.DictWriter(file, headers, delimiter='\t')
    write_into_file.writeheader()
    write_into_file.writerows(data)

