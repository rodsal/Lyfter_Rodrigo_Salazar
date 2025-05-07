def sum (actual_value, input_number):
    return actual_value + input_number

def substract (actual_value, input_number):
    return actual_value - input_number

def multiply (actual_value, input_number):
    return actual_value * input_number

def divide (actual_value, input_number):
    return actual_value / input_number

def delete_result():
    return 0

def show_menu():
    print("------- Menu -------")
    print("1. Sumar")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Borrar resultado")
    print("6. Salir")
    print()

def read_option():
    continue_reading_options = True
    while continue_reading_options:
        try:
            option = int(input("Seleccione una opcion: "))
            print()
            if option >= 1 and option <= 4:
                input_value = read_values()
                continue_reading_options = False
                return option, input_value
            elif option == 5 or option == 6:
                continue_reading_options = False
                return option, 0
            else:
                raise IndexError()
        
        
        except ValueError as error:
            print("La opción seleccionada no es un número. Favor ingresar un número del 1 al 6 como depsliega el menú")
            pass
        except IndexError as index_error:
            print("Las opciones a seleccionar son solo del 1 al 6. Favor intentar con solo esas posibilidades")
            pass
        

def read_values():
    while True:
        try:
            input_value = int(input("Seleccione el número: "))
            print()
            return input_value
        except ValueError as error:
            print("El valor ingresado no es un número. Favor volver a intentarlo con un número")
            pass

def option_excecution(pOption,input_value, actual_number):
    continuar = True
    if(pOption == 1):
        result = sum(actual_number, input_value)
        print("EL resutlado de la suma es: " + str(result))
    elif(pOption == 2):
        result = substract(actual_number, input_value)
        print("EL resutlado de la resta es: " + str(result))
    elif(pOption == 3):
        result = multiply(actual_number, input_value)
        print("EL resutlado de la multiplicación es: " + str(result))
    elif(pOption == 4):
        result = divide(actual_number, input_value)
        print("EL resutlado de la división es: " + str(result))
    elif (pOption == 5):
        result = delete_result()
    elif(pOption == 6):
        continuar = False
        result = 0
    return continuar, result
    #else:
    #    print("La opcion selecionada es inválida")


continue_running = True
actual_number = 0
while(continue_running):
    try:
        show_menu()
        print("El número actual es: " + str(actual_number))
        selected_option,input_value = read_option()
        continue_running, result = option_excecution(selected_option,input_value,actual_number)
        actual_number = result
        
    except Exception as general_exception:
        print("An excpetion occured: " + str(general_exception))
        continue_running = False
