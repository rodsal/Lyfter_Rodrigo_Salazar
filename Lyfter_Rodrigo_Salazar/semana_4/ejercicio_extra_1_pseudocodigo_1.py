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