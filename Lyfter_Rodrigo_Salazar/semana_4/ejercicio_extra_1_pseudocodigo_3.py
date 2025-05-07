
primero = int(input("Esciba el primer numero: "))
segundo = int(input("Esciba el segundo numero: "))

if primero > segundo:
    numero_temporal = primero
    primero = segundo
    segundo = numero_temporal

print ("primero " + str(primero) + "    segundo: " + str(segundo))
