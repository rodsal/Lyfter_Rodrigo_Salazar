from Student import Student

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
        name = input("Escriba el nombre completo del estudiante: ")
        section = input("Escriba la sección del estudiante: ")
        spanish_grade = validate_grade("Español")
        english_grade = validate_grade("Ingles")
        ss_grade = validate_grade("Estudios Sociales")
        science_grade = validate_grade("Ciencias")
        
        new_student = Student(name, section, spanish_grade, english_grade, ss_grade,science_grade)
        return new_student

def calculate_average(sum_grades):
    average = sum_grades/4
    return average

def top_3_students(averages_per_student):
    top_3 = sorted(averages_per_student.items(), key=lambda x: x[1], reverse=True)[:3]
    return top_3

def display_top_3 (top_3):
    print("Estos son los 3 mejores estudiantes y sus notas: ")
    for name,grade in top_3:
        print("Nombre: " + name + " - Notas: " + str(grade))
        print("---------------------------------------")

def average_students_grades (averages_per_student):
    final_average = 0
    for name in averages_per_student:
        final_average = final_average + averages_per_student[name]
    final_average = final_average/len(averages_per_student)
    return final_average

def display_final_average(final_average):
    print ("El promedio final de todos los estudiantes es: " + str(final_average))
    print("---------------------------------------------")

def request_student_dictionary(dic_student):
    name = dic_student["nombre_completo"]
    section = dic_student["section"]
    spanish_grade = dic_student["nota_español"]
    english_grade = dic_student["nota_ingles"]
    ss_grade = dic_student["nota_estudios_sociales"]
    science_grade = dic_student["nota_ciencias"]
    new_student = Student(name, section, spanish_grade, english_grade, ss_grade,science_grade)
    return new_student






