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