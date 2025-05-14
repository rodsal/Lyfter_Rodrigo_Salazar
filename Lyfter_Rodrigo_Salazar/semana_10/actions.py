

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

def calculate_students_average(students):
    
    averages_per_student = {}
    for student in students:
        average = 0
        sum_grades = 0
        for key in student:
            if "nota" in key:
                sum_grades = sum_grades + int(student[key])
        average = calculate_average(sum_grades)
        averages_per_student[student["nombre_completo"]] = average
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

def display_student_info(students):
    for student in students:
        for key in student:
            print(key + ": " + str(student[key]))
        print("---------------------------------------")












