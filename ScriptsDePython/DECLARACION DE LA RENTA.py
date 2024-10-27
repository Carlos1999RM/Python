
#DECLARACION DE LA RENTA:

#Para tributar en un determinado país es necesario ser mayor de edad y cobrar más de 1000 euros
#al mes. Además los tramos impositivos de la renta anual son los siguientes:
#RENTA TIPO IMPOSITIVO
#Menos de 15.000 eu 5%
#Entre 15.000 y 25.000 eu 15%
#Entre 25.000 y 35.000 eu 20%
#Entre 35.000 y 60.000 eu 30%
#Más de 60.000 eu 45%
#Escribe un script que primero compruebe si eres susceptible de que se te aplique algún tipo
#impositivo y en caso afirmativo imprima por pantalla cuál te tocaría.

# Pedir datos al usuario
# edad
edad = int(input("Ingresa tu edad: "))
# ingresos
ingresos = float(input("Introduce tu ingresos mensuales: "))




# Comprobar si se debe aplicar el tipo impositivo y comprobar cual
# Comprobar si el uaurio es mayor de edad y sus ingresos -->
if edad >= 18 and ingresos>1000:
    print("Eres susceptible de tributar.")
    # Calcular renta anual
    renta_anual = ingresos * 12
    ## Comprobar en que tramo se encuentra su ingreso anual
    if renta_anual < 15000:
        print("Tu tipo impositivo es del 5%")
    elif 15000 <= renta_anual < 25000:
        print("Tu tipo impositivo es del 15%")
    elif 25000 <= renta_anual < 35000:
        print("Tu tipo impositivo es del 20%")
    elif 35000 <= renta_anual < 60000:
        print("Tu tipo impositivo es del 45%")


# Si el usuario no está en el rango de edad o ingresos
else:
# Imprimir que no tiene obligación de tributar
    print("No eres susceptible a tributar.")