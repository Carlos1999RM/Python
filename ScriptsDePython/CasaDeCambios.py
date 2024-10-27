#CASA DE CAMBIOS: 

#Una casa de cambios necesita construir un programa que dada una cantidad de euros introducida 
#por el usuario de el resultante en dólares.

# --- Pedir al usuario el montante oportuno ---#

def euros_a_dolares(euros):
    tasa_de_cambio = 1.09 # 1 EU = 1.2 $
    dólares = euros * tasa_de_cambio
    return dólares

#  Solicitar la cantidad de euros al usuario
euros = float(input("Introduce la cantidad de euros: "))

# Converir a dólares
dólares = euros_a_dolares(euros)

# Mostrar el resultado
tasas_de_gestión = dólares * 0.1

## Calculamos cantidad de dólares que recibe el usuario
dolares_recibidos = dólares - tasas_de_gestión

## Imptimimos el desglose de la operación
print("Monto ingresado: ", euros, "euros")
print("Cambio en dólares", dólares, " dólares")
print("Tasas de gestión: ", tasas_de_gestión, " dólares")
print("Monto recibido: ", dolares_recibidos, " dólares")