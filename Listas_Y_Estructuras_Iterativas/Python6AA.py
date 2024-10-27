#LISTAS NUMERICAS:
#1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros: [1,2,3,4,5,6,7,8,9,10].
#2. Crea una nueva lista con los números pares de la lista anterior en orden inverso
#3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por
#consola.
#4. Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de
#compresión).
#5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
#6. Haz lo mismo con el número más alto
#7. Suma todos los elementos de la lista con y sin un bucle.
#8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras
#el punto 2.

# <!-- ################################################################ --¡>

#1. Crea una lista llamada “numeros“ que contenga los siguientes numeros enteros: [1,2,3,4,5,6,7,8,9,10].
#numeros = [0,1,2,3,4,5,6,7,8,9,10]
numeros = list(range(1,11))

# <!-- ################################################################ --¡>

#2. Crea una nueva lista con los números pares de la lista anterior en orden inverso
# Paso 1: Generar la lista de números pares del 2 al 20
numeros_pares = list(range(2, 10, 2))

# <!-- ################################################################ --¡>

# Paso 2: Invertir el orden de la lista
numeros_pares_inverso = numeros_pares[::-1]

# Mostrar la lista resultante
#print(numeros_pares_inverso)

# <!-- ################################################################ --¡>

#3. Escribe un bucle que recorra la lista “numeros“ e imprima el cuadrado de cada numero por
# consola.
#for numero in numeros:
    #print(f"El cuadrado de {numero} es {numero ** 2}")

# <!-- ################################################################ --¡>

#4. Intenta rehacer los pasos 2 y 3 con el menor número de lineas posible (método de
#compresión).
#print(list(range(2, 10, 2))[::-1])

# <!-- ################################################################ --¡>

#5. Usa un método que te devuelva el número más pequeño de la lista e imprímelo por pantalla
#def número_minimo(lista):
    # Encuentra el número más pequeño en la lista
    #minimo = min(lista)
    # Imprime el número más pequeño
    #print(minimo)
    # Devuelve el número más pequeño
    #return(minimo)


    # Ejemplo de uso
#número_minimo(numeros)

# <!-- ################################################################ --¡>

#6. Haz lo mismo con el número más alto
#def números_máximo(listilla):
    # Encuentra el número más pequeño
    #máximo = max(listilla)
    # Imprime el número más grande
    #print(máximo)
    # Devuleve el número más alto
    #return máximo

    # Ejemplo de uso
#números_máximo(numeros)

# <!-- ################################################################ --¡>

#7. Suma todos los elementos de la lista con y sin un bucle.
def sumar_elementos(lista):
    # Suma todos los elementos de la lista
    suma = sum(lista)
    # Imprime la suma de los elementos
    print(suma)
    # Devuelve la suma de los elementos
    return suma

# Ejemplo de uso
sumar_elementos(numeros)

# <!-- ################################################################ --¡>

# 8. Encuentra el índice correspondiente al número 8 en la lista original y en la lista resultante tras
# el punto 2.

# Paso 1: Generar la lista de números pares
#numeros_pares = list(range(2, 10, 2))
# Paso 2: Invertir el orden de la lista
#numeros_pares_inverso = numeros_pares[::-1]
# Paso 3: Encontrar el índice del número 8 en la lista original
indice_oroginal = numeros_pares.index(8)
# Paso 4: Encontrar el índice del número 8 en la lista invertida
indice_inverso = numeros_pares_inverso.index(8)
# Mostrar los índices
print("Índice del número 8 en la lista original:", indice_oroginal)
print("Índice del número 8 en la lista invertida: ", indice_inverso)

# <!-- ################################################################ --¡>
