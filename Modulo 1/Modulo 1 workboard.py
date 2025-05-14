import random

"""
segundos = int(input("Escriba un tiempo en segundos: "))
segundos_convertidos = segundos / 60
if segundos_convertidos > 10:
    resultado = "Mayor"
else:
    if segundos_convertidos == 10:
        resultado = "Igual"
    else:
        resultado = str((10 - segundos_convertidos) * 60)
print (resultado)



numero_inicial = int(input("Escriba un numero: "))
suma = 0
for numero in range(numero_inicial):
    suma = suma + (numero +1)
print (suma)


primero = int(input("Esciba el primer numero: "))
segundo = int(input("Esciba el segundo numero: "))


if primero > segundo:
    numero_temporal = primero
    primero = segundo
    segundo = numero_temporal

print ("primero " + str(primero) + "    segundo: " + str(segundo))


velocidad_km_h = int(input("Escriba una velocidad en km/h: "))
conversion = (1000/3600) *velocidad_km_h

print (conversion)

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)

numero_adivinado = False
while numero_adivinado == False:
    numero_supuesto = int(input())
    if numero_aleatorio == numero_supuesto:
        numero_adivinado = True



num_1 = int(input("Escriba el primer numero: "))
num_2 = int(input("Escriba el segundo numero: "))
num_3 = int(input("Escriba el tercer numero: "))

if num_1 == 30 or num_2 == 30 or num_3 == 30 or (num_1+num_2+num_3) == 30:
    print ("Correcto")
else:
    print("incorrecto")



num_1 = int(input("Escriba un numero: "))
num_2 = int(input("Escriba un segundo numero: "))
num_3 = int(input("Escriba un tercer numero: "))
num_4 = int(input("Escriba un cuarto numero: "))
num_5 = int(input("Escriba un quinto numero: "))

mayor = max(num_1,num_2,num_3,num_4,num_5)
print(mayor)

"""


# 💪🏽 **Ejercicios**

# 1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
#     1. Si le salen errores, **no se asuste.** Lealos e intente comprender qué significan.
#     *Los errores son oportunidades de aprendizaje.*
#     2. Por ejemplo:
#         1. string + string → ?
#text_1 = "Hola"
#text_2 = "Mundo"
#print (text_1+text_2)
#         2. string + int → ?
#text_1 = "Hola Mundo"
#number_1 = 34
#print(text_1+number_1)
#         3. int + string → ?
#print(number_1+text_1)
#         4. list + list → ?
#list_1 = [2,3,4,5]
#list_2 = ["papaya", "chayote", "vainicas"]
#print (list_1+list_2)
#         5. string + list → ?
#text_3 = "manzana"
#print(list_2+text_3)
#         6. float + int → ?
#float_1 = 34.6
#print(number_1+float_1)
#         7. bool + bool → ?
#bool_1 = True
#bool_2 = False

#print(bool_1+bool_2)


# 2. Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
"""
name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))

if age > 0 and age <= 3:
    print("bebé")
elif age > 3 and age <= 9:
    print("niño")
elif age > 9 and age <= 12:
    print("preadolecente")
elif age > 12 and age <= 18:
    print("adolecencia")
elif age > 18 and age <= 40:
    print("adulto joven")
elif age > 41 and age <= 65:
    print("adulto")
elif age > 65 and age <= 120:
    print("adulto mayor")
else:
    print("Edad no valida")
"""

# 3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
#     1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
"""
secret_number = random.randint(1,10)

secret_number_found = False

while secret_number_found == False:
    number_guessed = int(input("Adivine un numero del 1 al 10: "))
if number_guessed == secret_number:
        secret_number_found = True
"""

# 4. Cree un programa que le pida tres números al usuario y muestre el mayor.
"""
number_1 = int(input("Escriba el primer numero: "))
number_2 = int(input("Escriba el segundo numero: "))
number_3 = int(input("Escriba el tercer numero: "))

if number_1 > number_2 and number_1 > number_3:
    print("Numero 1 es mayor")
elif number_2 > number_1 and number_2 > number_3:
    print("Numero 2 es mayor")
elif number_3 > number_1 and number_3 > number_2:
     print("Numero 3 es mayor")
else:
     print("Los 3 numeros son iguales")

"""
# 5. Dada `n` cantidad de notas de un estudiante, calcular:
#     1. Cuantas notas tiene aprobadas (mayor a 70).
#     2. Cuantas notas tiene desaprobadas (menor a 70).
#     3. El promedio de todas.
#     4. El promedio de las aprobadas.
#     5. El promedio de las desaprobadas.
"""
grade_counter = 0
approved_grades_qunatity = 0
disapprove_grade_quantity = 0
approved_grades_percentage = 0
disapprove_grade_percentage = 0
total_grades_percenatge = 0

grades_quantity = int(input("Ingrese la cantidad de notas: "))
while grade_counter < grades_quantity:
    grade_counter = grade_counter + 1
    actual_grade = int(input("Ingrese la nota numero " + str(grade_counter) + ": "))
    if actual_grade < 70:
        disapprove_grade_quantity = disapprove_grade_quantity + 1
        disapprove_grade_percentage = disapprove_grade_percentage + actual_grade
    else:
        approved_grades_qunatity = approved_grades_qunatity + 1
        approved_grades_percentage = approved_grades_percentage + actual_grade
    total_grades_percenatge = total_grades_percenatge + (actual_grade/grades_quantity)

if disapprove_grade_quantity > 0:
    disapprove_grade_percentage = disapprove_grade_percentage/disapprove_grade_quantity
if approved_grades_qunatity > 0:
    approved_grades_percentage = approved_grades_percentage/approved_grades_qunatity

print("El estudiante tiene esta cantidad de notas aprobadas: " + str(approved_grades_qunatity))
print("El promedio de las notas aprobadas: " + str(approved_grades_percentage))

print("El estudiante tiene esta cantidad de notas desaprobadas: " + str(disapprove_grade_quantity))
print("El promedio de las notas desaprobadas: " + str(disapprove_grade_percentage))   

print("Este es el primedio total de notas: " + str(total_grades_percenatge))
"""   

#1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
#    1. Ejemplos:
#    2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
#    `second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->
#    Hay casos
#    en los
#    que la
#    iteracion por
#    indice es
#    muy util
"""
first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

for index in range(len(first_list)):
    print (first_list[index] + " " + second_list[index])
"""               

#2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
#1. Pista: investigue de que otras maneras se puede usar el `range`.
#    2. Ejemplos:
#    3. `my_string = ‘Pizza con piña’` → 
#    a
#    ñ
#    i
#    p
    
#    n
#    o
#    c
    
#    a
#    z
#    z
#    i
#    p

"""
text_to_reverse = "Pizza con piña"

for index in range(len(text_to_reverse) -1,-1,-1):
    print(text_to_reverse[index])
"""

#3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
#    1. Ejemplos:
#    2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`
"""
list_to_modify = [4, 3, 6, 1, 7]
last_item = list_to_modify.pop(len(list_to_modify)-1)
first_item = list_to_modify.pop(0)

list_to_modify.insert(0,last_item)
list_to_modify.insert(len(list_to_modify), first_item)
print(list_to_modify)
"""

#4. Cree un programa que elimine todos los números impares de una lista.
#    1. Ejemplos:
#    2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`
"""
number_list = [1,2,3,4,5,6,7,8,9,10,11,11,11,11,11]

for number in number_list:
    if number % 2 != 0:
        number_list.remove(number)
print(number_list)
"""
#correccion ejercicio
"""
number_list = [1,2,3,4,5,6,7,8,9,10,11,11,11,11,11]
pair_number_list = []
for number in number_list:
    if number % 2 == 0:
        pair_number_list.append(number)
print(pair_number_list)
"""

#5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
#    1. Ejemplos:
#    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [54, 86, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

"""
num_1 = int(input("Ingrese el numero 1 "))
num_2 = int(input("Ingrese el numero 2 "))
num_3 = int(input("Ingrese el numero 3 "))
num_4 = int(input("Ingrese el numero 4 "))
num_5 = int(input("Ingrese el numero 5 "))
num_6 = int(input("Ingrese el numero 6 "))
num_7 = int(input("Ingrese el numero 7 "))
num_8 = int(input("Ingrese el numero 8 "))
num_9 = int(input("Ingrese el numero 9 "))
num_10 = int(input("Ingrese el numero 10 "))

numbers = []
numbers.append(num_1)
numbers.append(num_2)
numbers.append(num_3)
numbers.append(num_4)
numbers.append(num_5)
numbers.append(num_6)
numbers.append(num_7)
numbers.append(num_8)
numbers.append(num_9)
numbers.append(num_10)

high_number = max(numbers)
print(str(numbers) + ". El más alto fue " + str(high_number))
"""


#<aside>
#💪🏽 **Ejercicios**
#
#1. Cree un diccionario que guarde la siguiente información sobre un hotel:
#    - `nombre`
#    - `numero_de_estrellas`
#    - `habitaciones`
#- El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
#    - `numero`
#    - `piso`
#    - `precio_por_noche`
"""
diccionary_hotel = {
    "nombre": "Hotel Bouganvillea",
    "numero_de_estrellas": 4,
    "habitaciones": [
        {
            "numero": 1,
            "piso": 1,
            "precio_por_noche": 234
        },
        {
            "numero": 2,
            "piso": 1,
            "precio_por_noche": 234
        },
        {
            "numero": 3,
            "piso":2,
            "precio_por_noche":358
        },
        {
            "numero": 4,
            "piso": 2,
            "precio_por_noche": 358
        }

    ]
}
"""

#2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
#    1. Ejemplos:
#    2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
#    `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
#    → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`
"""
list_keys = ["fruta", "verdura", "legumbre", "proteina"]
list_values = ["papaya", "camote", "frijoles", "pescado"]
list_to_diccionary = {}
for index in range(len(list_keys)):
    list_to_diccionary[list_keys[index]] = list_values[index]
"""

#3. Cree un programa que use una lista para eliminar keys de un diccionario.
#    1. Ejemplos:
#    2. `list_of_keys = [’access_level’, ‘age’]`
#    `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
#    → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`
#</aside>

"""
list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

for key in list_of_keys:
    employee.pop(key)

print(employee)
"""

#Ejercicios Extra
#Dada una lista de ventas con la siguiente información:
#   date
#   customer_email
#   items
#Y cada item teniendo la siguiente información:
#   name
#   upc
#   unit_price
#Cree un diccionario que guarde el total de ventas de cada UPC.
#Ejemplos:
sales = [
	{
		'date': '27/02/23',
		'customer_email': 'joe@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Iron',
				'upc': 'ITEM-324',
				'unit_price': 32.45,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 12.54,
			},
		],
	},
	{
		'date': '27/02/23',
		'customer_email': 'david@gmail.com',
		'items': [
			{
				'name': 'Lava Lamp',
				'upc': 'ITEM-453',
				'unit_price': 65.76,
			},
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 5.42,
			},
		],
	},
	{
		'date': '26/02/23',
		'customer_email': 'amanda@gmail.com',
		'items': [
			{
				'name': 'Key Holder',
				'upc': 'ITEM-23',
				'unit_price': 3.42,
			},
			{
				'name': 'Basketball',
				'upc': 'ITEM-432',
				'unit_price': 17.54,
			},
		],
	},
]
"""
total_per_upc = {}

for key in sales:
    for items in key["items"]:
        type = items["upc"]
        value = items["unit_price"]
        if type not in total_per_upc:
            total_per_upc[type] = 0
            total_per_upc[type] += value

print(total_per_upc)
"""

#----------------------------------------------------------------------------------------

#<aside>
#💪🏽 **Ejercicios**
#1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
"""
def return_sum_with_text():
    sum = sum_of_numbers(5,6)
    return "La suma de los dos numeros es: " + str(sum)


def sum_of_numbers(num_1,num_2):
    return num_1 + num_2

print (return_sum_with_text())
"""

#2. Experimente con el concepto de scope:
#    1. Intente accesar a una variable definida dentro de una función desde afuera.
"""
def multiply_numbers(num_a, num_b):
    multiply = num_a * num_b
    return multiply

print(multiply)
"""
#    2. Intente accesar a una variable global desde una función y cambiar su valor.
"""
global_varibale = 5

def funcion_1():
    global_varibale = 7
    return global_varibale
print(funcion_1())
"""

#3. Cree una función que retorne la suma de todos los números de una lista.
#    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
#    2. [4, 6, 2, 29] → 41
"""
def sum_of_list (in_list):
    total_sum = 0
    for number in in_list:
        total_sum = total_sum + number
    return total_sum

list_to_sum = [47, 62, 29, 29]
print(sum_of_list(list_to_sum))
"""

#4. Cree una función que le de la vuelta a un string y lo retorne.
#    1. Esto ya lo hicimos en iterables.
#    2. “Hola mundo” → “odnum aloH”
"""
def revert_text(text):
    reversed_string = ""
    for index in range(len(text) -1,-1,-1):
        reversed_string = reversed_string + text[index]
    return reversed_string

string_to_reverse = "Hola mundo"
print(revert_text(string_to_reverse))
"""

#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
#    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”

"""
def print_upper_lower_cases(text):
    lower_count = 0
    upper_count = 0
    for word in text.replace(" ",""):
        if word.isupper():
            upper_count += 1
        else:
            lower_count += 1
    return lower_count, upper_count

text_to_validate = "I lovE NacióN Sushi"
print(print_upper_lower_cases(text_to_validate))
"""

#6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
#    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
#    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

"""
def order_text_by_alphabet (text):
    text_splitted = text.split("-")
    text_splitted.sort()
    text_ordered = ""
    for index in range(len(text_splitted)):
        if index != 0:
            text_ordered = text_ordered + "-" + text_splitted[index]
        else:
            text_ordered = text_ordered + text_splitted[index]
    return text_ordered

text_to_order = "python-variable-funcion-computadora-monitor"
print(order_text_by_alphabet(text_to_order))
"""
#7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#    2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#    3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*
#</aside>
"""
def return_prime_number(list_of_numbers):
    prime_number_list = []
    for number in list_of_numbers:
        if is_prime_number(number):
            prime_number_list.append(number)
    return prime_number_list

def is_prime_number(number):
    if number < 2:
        return False
    for division in range(2, number):
        if number % division == 0:
            return False
    return True

list_to_validate = [1, 4, 6, 7, 13, 9, 67]
print(return_prime_number(list_to_validate))
"""
#1. Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
#    1. Suma
#    2. Resta
#    3. Multiplicación
#    4. División
#    5. Borrar resultado
#Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. 
#El resultado debe pasar a ser el nuevo numero actual.
#Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer 
# la operación.
"""
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
"""
    
#Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados 
#alfabéticamente.
"""
def read_file(path):
    songs_list = []
    with open(path) as file:
        for line in file.readlines():
            songs_list.append(line)
    return songs_list

def write_file(path,list):
    with open(path, "w", encoding='utf-8') as file:
        for song in list:
            file.write(song)
            file.

path = "/Users/nicoleportuguez/Library/Mobile Documents/com~apple~CloudDocs/Lyfter/Modulo 1/Semana 8/Ejercicio manejo de archivos/Lista_de_canciones"
song_list = read_file(path)
song_list.sort()
write_file(path,song_list)
"""

#1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
#    1. Debe incluir:
#        1. Nombre
#        2. Género
#        3. Desarrollador
#        4. Clasificación ESRB
#    2. Ejemplo de archivo final:
#        
#        ```
#        nombre,genero,desarrollador,clasificacion
#        Grand Theft Auto IV,Accion,Rockstar Games,M
#        The Elder Scrolls IV: Oblivion,RPG,Bethesda,M
#        Tony Hawk's Pro Skater 2,Deportes,Activision,T
#        ```
import csv
"""
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
"""

#2. Lea sobre el resto de métodos del módulo `csv` [aqui](https://docs.python.org/es/3/library/csv.html) y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por *tabulaciones* en vez de por *comas*.
#    1. Ejemplo de archivo final:
#        
#        ```
#        nombre	genero	desarrollador	clasificacion
#        Grand Theft Auto IV	Accion	Rockstar Games	M
#        The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
#        Tony Hawk's Pro Skater 2	Deportes	Activision	T
#        ```
"""
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
  with open(path, 'w',encoding='utf-8') as file:
    write_into_file = csv.DictWriter(file, headers, delimiter='\t')
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
"""

#2. Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON ([Archivos JSON](https://www.notion.so/Archivos-JSON-79f9758cb59d4452a9c8668efa25356c?pvs=21)).
#    1. Debe leer el archivo para importar los Pokémones existentes.
#    2. Luego debe pedir la información del Pokémon a agregar.
#    3. Finalmente debe guardar el nuevo Pokémon en el archivo.
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

#dev
"""
with open('/Users/nicoleportuguez/Library/Mobile Documents/com~apple~CloudDocs/Lyfter/Modulo 1/Semana 8/Ejercicio Manejo de Json/Pokemon.json', 'r') as json_to_read:
    pokemon_json = json.load(json_to_read) 


for index in range(len(pokemon_json)):
    print(str(index+1)+". "+ pokemon_json[index]["name"]["english"])

seleccion_pokemon = int(input("Escoja el numero del pokemon a seleccionar: "))
print("Su seleccion fue: " + pokemon_json[seleccion_pokemon-1]["name"]["english"])
if seleccion_pokemon <= len(pokemon_json):
    print("Tipo: " + ": " + pokemon_json[seleccion_pokemon-1]["type"][0])
    for key in pokemon_json[seleccion_pokemon-1]["base"]:
        print(str(key) + ": " + str(pokemon_json[index]["base"][key]))
    

    

name = input("escriba el nombre del Pokemon: ")
type = input("Escriba el tipo del Pokemon: ")
pokemon_hp = int(input("Escriba el HP del Pokemon: "))
attack = int(input("Escriba el ataque del Pokemon: "))
defense = int(input("Escriba la defensa del Pokemon: "))
sp_attack = int(input("Escriba el ataque sp del Pokemon: "))
sp_defense = int(input("Escriba la defensa sp del Pokemon: "))
speed = int(input("Escriba la volicddad del Pokemon: "))

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
pokemon_json.append(add_pokemon)
with open ('/Users/nicoleportuguez/Library/Mobile Documents/com~apple~CloudDocs/Lyfter/Modulo 1/Semana 8/Ejercicio Manejo de Json/Pokemon.json','w') as json_pokemon_file:
    json.dump(pokemon_json,json_pokemon_file, indent=4)
"""


