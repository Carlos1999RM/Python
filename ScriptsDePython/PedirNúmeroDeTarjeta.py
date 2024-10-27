#### Pedir al usuario que ingrese el número de tarjeta ####
#num_tarjeta = input("Ingresa tú número de tarjeta ")

### Introduce los números ###
#print("**** **** ****", num_tarjeta[12:16])

#<!------------------------------------------------------------------->
# Pedir al usuario que ingrese el número de tarjeta
num_tarjeta = input("Ingresa número de tarjeta: ")

# Asegurarse de que el número tenga al menos 16 caracteres
if len(num_tarjeta.replace("","")) >= 16:
    #Imprimir el número de tarjeta oculto
    print("**** **** ****", num_tarjeta[-4:])
else:
    print("El número no es válido")