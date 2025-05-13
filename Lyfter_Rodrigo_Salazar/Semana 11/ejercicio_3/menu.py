import data
import os
import actions

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

def option_execution(option,students):
    try:
        
        path = "students_data_export.csv"
        continue_running = True
        if(option == 1):
            new_student = actions.request_student_info()
            students.add_student(new_student)

        elif (option == 2):
            students.display_all_students()

        elif (option == 3):
            average_per_student = students.calculate_students_average()
            top_3 = actions.top_3_students(average_per_student)
            actions.display_top_3(top_3)

        elif (option == 4):
            average_per_student = students.calculate_students_average()
            final_average = actions.average_students_grades(average_per_student)
            actions.display_final_average(final_average)

        elif (option == 5):
            students_to_dic = students.convert_to_dictionary()
            data.write_csv(path, students_to_dic, students_to_dic[0].keys())
            print("El archivo fue exportado exitosamente. Con el nombre " + path)

        elif (option == 6):
            try:
                import_path = data.request_import_file()
                if os.path.exists(import_path):
                    dic_students = data.read_file(import_path)
                    students.convert_from_dictionary(dic_students)
                else:
                    raise FileExistsError
            except FileExistsError as error:
                print("El archivo solicitado no existe, favor intente con otro")

        else:
            continue_running = False
        return continue_running
    
    except Exception as exception:
        print("Hubo un error de ejecución " + exception)
        



