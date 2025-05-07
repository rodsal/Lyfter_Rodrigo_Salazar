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
