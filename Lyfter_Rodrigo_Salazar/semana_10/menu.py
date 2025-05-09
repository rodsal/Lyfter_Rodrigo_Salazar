import actions
import data
import os

def show_menu(): 
    print("------- Bienvenido al sistema del colegio Lyfter -------")
    print("1. Ingresar la información de Estudiante")
    print("2. Ver la información de los Estudiantes")
    print("3. Ver el top 3 de los mejores estudiantes")
    print("4. Ver el promedio de notas de todos los Estudiantes")
    print("5. Exportar los estudiantes a un archivo CSV")
    print("6. Importar los datos de un CSV previamente exportado")
    print("7. Salir")

def read_option():
    continue_reading_options = True
    while continue_reading_options:
        try:
            option = int(input("Seleccione una opcion: "))
            print()
            if option >= 1 and option <= 7:
                continue_reading_options = False
                return option    
            else:
                raise IndexError

        except ValueError as error:
            print("La opción seleccionada no es un número. Favor ingresar un número del 1 al 7 como depsliega el menú")
            pass
        except IndexError as index_error:
            print("Las opciones a seleccionar son solo del 1 al 7. Favor intentar con solo esas posibilidades")
            pass

def option_execution(option,path):
    #try:
    continue_running = True
    if os.path.exists(path):
        students = data.read_student_info(path)
    else:
        students = []
    if(option == 1):
        student_name, student_section, spanish_grade, english_grade, ss_grade, science_grade = actions.request_student_info()
        add_student = data.add_to_json_format(student_name,student_section,spanish_grade, english_grade,ss_grade, science_grade)
        students.append(add_student)
        try:
            data.write_json_to_file(students,path)
        except Exception as exception:
            print("Hubo un error conviertiendo el file en csv " + exception)
    elif (option == 2):
        actions.display_student_info(students)
    elif (option == 3):
        average_per_student = actions.calculate_students_average(students)
        top_3 = actions.top_3_students(average_per_student)
        actions.display_top_3(top_3)
    elif (option == 4):
        average_per_student = actions.calculate_students_average(students)
        actions.display_students_averages(average_per_student)
    elif (option == 5):
        pass
    elif (option == 6):
        pass
    else:
        continue_running = False
    return continue_running
    #except Exception as exception:
    #    print("Hubo un error de ejecución " + exception)
        



