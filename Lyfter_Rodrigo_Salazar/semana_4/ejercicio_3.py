import random
secret_number = random.randint(1,10)

secret_number_found = False

while secret_number_found == False:
    number_guessed = int(input("Adivine un numero del 1 al 10: "))
    if number_guessed == secret_number:
        secret_number_found = True