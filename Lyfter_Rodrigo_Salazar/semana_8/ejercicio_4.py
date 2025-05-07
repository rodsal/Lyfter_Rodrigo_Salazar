import json

def read_json_file(path):
    try:
        with open(path, 'r') as json_to_read:
            pokemon_json = json.load(json_to_read)  
        return pokemon_json
    except json.JSONDecodeError:
        print("El archivo está vacío o contiene un JSON inválido.")
        raise

def show_menu(): 
    print("------- Bienvenido a la Pokemon -------")
    print("Que desea hacer?")
    print("1. Ver un Pokemon.")
    print("2. Agregar un Pokemon")
    print("3. Salir")

def read_option():
    continue_reading_options = True
    while continue_reading_options:
        try:
            option = int(input("Seleccione una opcion: "))
            print()
            if option >= 1 and option <= 3:
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

def option_execution(option,json,path):
    continue_running = True
    if(option == 1):
        display_pokemon(json)
        select_pokemon_number = select_pokemon(json)
        display_pokemon_info(json, select_pokemon_number)
    elif (option ==2):
        name,type,pokemon_hp,attack,defense,sp_attack,sp_defense,speed = get_pokemon_info()
        info_pokemon = add_pokemon_info_to_format(name,type,pokemon_hp,attack,defense,sp_attack,sp_defense,speed)
        json_new_pokemon = add_pokemon_to_json(info_pokemon,json)
        write_json_to_file(json_new_pokemon, path)
    
    else:
        continue_running = False
    return continue_running

def display_pokemon(json):
    for index in range(len(json)):
        print(str(index+1)+". "+ json[index]["name"]["english"])

def select_pokemon(json):
    continue_selecting_pokemon = True
    while continue_selecting_pokemon:
        try:
            seleccion_pokemon = int(input("Escoja el numero del pokemon a seleccionar para ver en detalle: "))
            print(len(json))
            if seleccion_pokemon > len(json):
                raise IndexError
            else:
                continue_selecting_pokemon = False
            return seleccion_pokemon
            
        except ValueError as error:
            print("La opción seleccionada no es un número. Favor ingresar un número del 1 al 2 como depsliega el menú")
            pass
        except IndexError as error:
            print("Las opciones a seleccionar son solo las desplegadas en el menu. Favor intentar con solo esas posibilidades")
            pass


def display_pokemon_info(json, seleccion_pokemon):
    print("Su seleccion fue: " + json[seleccion_pokemon-1]["name"]["english"])
    if seleccion_pokemon <= len(json):
        print("Tipo: " + ": " + json[seleccion_pokemon-1]["type"][0])
        for key in json[seleccion_pokemon-1]["base"]:
            print(str(key) + ": " + str(json[seleccion_pokemon-1]["base"][key])) 

def get_pokemon_info():
    continue_running = True
    while continue_running == True:
        try:
            name = input("escriba el nombre del Pokemon: ")
            type = input("Escriba el tipo del Pokemon: ")
            pokemon_hp = int(input("Escriba el HP del Pokemon: "))
            attack = int(input("Escriba el ataque del Pokemon: "))
            defense = int(input("Escriba la defensa del Pokemon: "))
            sp_attack = int(input("Escriba el ataque sp del Pokemon: "))
            sp_defense = int(input("Escriba la defensa sp del Pokemon: "))
            speed = int(input("Escriba la volicddad del Pokemon: "))
            return name,type,pokemon_hp,attack,defense,sp_attack,sp_defense,speed

        except ValueError as error:
            print("Alguno de los valores de HP, Attack, Defense, SP Attack, SP Defense and speed no es número. Estos valores deben ser números")

def add_pokemon_info_to_format(name,type,pokemon_hp,attack,defense,sp_attack,sp_defense,speed):
    add_pokemon = {
      "name": {
        "english": name
      },
      "type": [
        type
      ],
      "base": {
        "HP": pokemon_hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
      }
    }
    return add_pokemon

def add_pokemon_to_json(add_pokemon,json):
    json.append(add_pokemon)
    return json

def write_json_to_file(pokemon_json, path):
    with open (path,'w') as json_pokemon_file:
        json.dump(pokemon_json,json_pokemon_file, indent=4)

continue_running = True
path = '/Users/nicoleportuguez/Library/Mobile Documents/com~apple~CloudDocs/Lyfter/Modulo 1/Semana 8/Ejercicio Manejo de Json/Pokemon.json'
while(continue_running):
    try:
        pokemon_json = read_json_file(path)
        show_menu()
        selected_option = read_option()
        continue_running = option_execution(selected_option,pokemon_json,path)
        
    except Exception as general_exception:
        print("An excpetion occured: " + str(general_exception))
        continue_running = False        
