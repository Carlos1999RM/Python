#EJERCICIOS HOJA 3
#TEMA: USO DE LISTAS Y BUCLES
#OBJETIVO: FAMILIARIZACIÓN CON EL USO DE LISTAS SIMPLES, LISTAS ANIDADAS, SUS
#FUNCIONES ASOCIADAS Y LAS SENTENCIAS CONDICIONALES Y LOS BUCLES EN EL
#CONTEXTO DE LAS LISTAS
#EJERCICIOS 3A
#BUCLES:

#1. Escribe un programa que pida al usuario un número entero y muestre por pantalla una
#estructura como la de más abajo, donde el valor de entrada es el número de estrellas en el
#centro de la estructura.
#*
#**
#***
#****
#*****
#****
#***
#**
#*

# <!-- ################################################################ --¡>

def imprimir_estructura(n):
    # Imprimir la parte ascendente

    for i in range(1, n + 1):
        print("#***#~" * i)

    # Imprimir la parte descendente
    for i in range(n -1,0, -1):
        print("#***#~"* i)

    # Que se repita por segunda vez(Es el mismo código que el de arriba)
    for i in range(1, n + 1):
        print("#***#~" * i)
      
    # Imprimir la parte descendente
    for i in range(n -1,0, -1):
        print("#***#~"* i)

# Solicitar al usuario un número entero
numero = int(input("Introduzca la anchura central (número entero): "))

# Llamar a la función para imprimir la estructura
imprimir_estructura(numero)