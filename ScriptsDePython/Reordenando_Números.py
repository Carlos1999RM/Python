# Solicitar al usuario que introduzca un número de más de una cifra
#numero = input("Introduce un número de más de una cifra: ")

# Comprobar que el número introducido es válido
#if len(numero) > 1 and numero.isdigit():
#    for digito in numero:
#        print(digito)
#    else: print("Por favor, introduce un número válido de 4 cifras.")

#### b. Script para invertir un número de cuatro cifras ####
# Solicitar al usuario que introduzca un número entero de cuatro cifras
#number = input("Introduce un número de cuatro cifras: ")

# Comprobar que el número introducido es válido
#if len(number) == 4 and number.isdigit():
    # Invertir el número
    #numero_invertido = number[::-1]
    # Imprimir el número invertido
    #print("El número invertidoes: ", numero_invertido)
#else:
    #print("Por favor, introduce un número válido de cuatro cifras.")

#<!------------------------------------------------------------------->

#RESTAURANTE:

#En un restaurante el menú consta de las siguientes opciones:
#Ensalada mixta   ————————   12 EU
#Sopa de pescado    ———————   10 EU
#Dorada al horno  ————————   18 EU
#Arroz al curry  —————————   14 EU
#Lasaña de carne     ———————   15 EU
#Brownie de chocolate    —————    8 EU
#Helado    ———————————    6 EU
#Refrescos    ——————————    5,5 EU
#Café    ————————————    3,5 EU
#Escribe un script que lea la cantidad de cada alimento consumido y que calcule e imprima el total 
#de la cuenta.

# Precios del menú
precios = {
     "Ensalada mixta": 12,
    "Sopa de pescado": 10,
    "Dorada al horno": 18,
    "Arroz al curry": 14,
    "Lasaña de carne": 15,
    "Brownie de chocolate": 8,
    "Helado": 6,
    "Refrescos": 5.5,
    "Café": 3.5
}


# Función para calcular el total
def calcular_total(consumos):
    total = 0
    for item, cantidad in consumos.items():
        total += precios[item] * cantidad
    return total


#Leer la cantidad de cada alimento consimido
consumos = {}
for item in precios.keys():
    cantidad = int(input(f"Introduce la cantidad de '{item}' consumida: "))
    consumos[item] = cantidad


# Calcular e imprimir el total
total = calcular_total(consumos)
print(f"El total de la cuenta es: {total} EU")