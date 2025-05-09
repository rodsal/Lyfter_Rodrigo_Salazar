

def validate_grade(subject):
    continue_asking = True
    while continue_asking:
        try:
            subject_grade = int(input("Ingrese la nota de " + subject + ": "))
            if subject_grade < 0 or subject_grade > 100:
                raise IndexError
            else:
                continue_asking = False
                return subject_grade
        except ValueError as error:
            print("Este campo debe ser un numero entre el 0 y el 100")
        except IndexError as error:
            print ("La nota no puede ser menor a 0 o mayor a 100")  

def request_student_info():
    student_name = input("Escriba el nombre completo del estudiante: ")
    student_section = input("Escriba la sección del estudiante: ")
    spanish_grade = validate_grade("Español")
    english_grade = validate_grade("Ingles")
    ss_grade = validate_grade("Estudios Sociales")
    science_grade = validate_grade("Ciencias")
    return student_name, student_section, spanish_grade, english_grade, ss_grade, science_grade

def calculate_average(sum_grades):
    average = sum_grades/4
    return average
"""
students = [
    {
        "nombre_completo": "Rodrigo Salazar",
        "section": "11C",
        "grades":
            {
            "nota_español": 70,
            "nota_ingles": 84,
            "social_studies_grade": 78,
            "nota_ciencias": 90
            }
    },
    {
        "nombre_completo": "Alvaro Jimenez",
        "section": "11A",
        "grades":
            {
            "nota_español": 90,
            "nota_ingles": 87,
            "social_studies_grade": 92,
            "nota_ciencias": 79
            }
    },
    {
        "nombre_completo": "Maria Gomez",
        "section": "11A",
        "grades":
            {
            "nota_español": 88,
            "nota_ingles": 81,
            "social_studies_grade": 73,
            "nota_ciencias": 75
            }
    },
    {
        "nombre_completo": "Nicole Mora",
        "section": "11B",
        "grades":
            {
            "nota_español": 72,
            "nota_ingles": 80,
            "social_studies_grade": 45,
            "nota_ciencias": 60
            }
    },
    {
        "nombre_completo": "Mario Fernandez",
        "section": "9A",
        "grades":
            {
            "nota_español": 70,
            "nota_ingles": 75,
            "social_studies_grade": 89,
            "nota_ciencias": 73
            }
    }
]
"""
def calculate_students_average(students):
    sum_grades = 0
    averages_per_student = {}
    for estudiante in students:
        average = 0
        grades = estudiante["grades"]
        sum_grades = sum(grades.values())
        average = calculate_average(sum_grades)
        averages_per_student[estudiante["nombre_completo"]] = average
    return averages_per_student

#for estudiante in students:
#    nombre = estudiante["nombre_completo"]
#    notas = estudiante["grades"]
#    promedio = sum(notas.values()) / len(notas)
#    print(f"{nombre} - Promedio: {promedio:.2f}")
            
            #sum_grades = sum_grades + grade
    #average = calculate_average (sum_grades)
    #print(average)

def top_3_students(averages_per_student):
    top_3 = sorted(averages_per_student.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_3

"""
student_name,student_section,spanish_grade,english_grade,ss_grade,science_grade = request_student_info()

print("Nombre: " + student_name)
print("Sección: " + student_section)
print("Nota de español: " + str(spanish_grade))
print("Nota de Inglés: " + str(english_grade))
print("Nota de Estudios Sociales: " + str(ss_grade))
print("Nota de Ciencias: " + str(science_grade))
"""

def display_top_3 (top_3):
    print("Estos son los 3 mejores estudiantes y sus notas: ")
    for name,grade in top_3:
        print("Nombre: " + name + " - Notas: " + str(grade))
        print("---------------------------------------")

def display_students_averages (averages_per_student):
    print("Estos son los estudiantes y sus proemdios")
    for name in averages_per_student:
        print("Nombre: " + name + " - Nota: " + str(averages_per_student[name]))
        print("---------------------------------------")

def display_student_info(students):
    for student in students:
        print("Nombre: " + student["nombre_completo"])
        print("Sección: " + student["section"])
        print("Notas:")
    
        for subject, grade in student["grades"].items():
            print("Materia: " + subject + " - Nota: " + str(grade))
        
        print("---------------------------------------")


        #grades = estudiante["grades"]
        #sum_grades = sum(grades.values())
        #average = calculate_average(sum_grades)
        #3averages_per_student[estudiante["nombre_completo"]] = average
    #return averages_per_student

#averages = calcular_promedio_estudiantes(students)
#top_3 = top_3_students(averages)
#display_top_3(top_3)
#display_students_averages(averages)
#display_student_info(students)


