import csv

def request_game_info():
    name = input("Ingrese el nombre del juego: ")
    gender = input("Ingrese el género del juego: ")
    developer = input("Ingrese el desarrollador del juego: ")
    classification = input("Ingrese la classificación ESRB: ")
    return name, gender, developer, classification

def convert_to_list():
    name,gender,developer,classification = request_game_info()
    game_list = {
            "nombre": name,
            "género": gender,
            "desarrollador": developer,
            "clasificacion": classification
        }
    
    return game_list

def show_menu(): 
    print("------- Bienvenido a la tienda Game Stop -------")
    print("1. Agregar juego.")
    print("2. Salir")

def read_option():
    continue_reading_options = True
    while continue_reading_options:
        try:
            option = int(input("Seleccione una opcion: "))
            print()
            if option >= 1 and option <= 2:
                continue_reading_options = False
                return option    
            else:
                raise IndexError

        except ValueError as error:
            print("La opción seleccionada no es un número. Favor ingresar un número del 1 al 2 como depsliega el menú")
            pass
        except IndexError as index_error:
            print("Las opciones a seleccionar son solo del 1 al 2. Favor intentar con solo esas posibilidades")
            pass

def option_execution(option):
    continue_running = True
    if(option == 1):
        game_list = convert_to_list()
    else:
        continue_running = False
        game_list = []
        
    return continue_running, game_list

def write_csv(path, data, headers):
  with open(path, 'w', encoding='utf-8') as file:
    write_into_file = csv.DictWriter(file, headers)
    write_into_file.writeheader()
    write_into_file.writerows(data)



continue_running = True
all_game_list = []
while(continue_running):
    try:
        show_menu()
        selected_option = read_option()
        continue_running, game_list = option_execution(selected_option)
        if len(game_list) > 1:
            all_game_list.append(game_list)
        print(all_game_list)
    except Exception as general_exception:
        print("An excpetion occured: " + str(general_exception))
        continue_running = False        

try:
    write_csv("data.csv",all_game_list,all_game_list[0].keys())
except Exception as exception:
    print("Hubo un error conviertiendo el file en csv " + exception)