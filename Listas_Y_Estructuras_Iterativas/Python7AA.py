#PILLANDO SOLTURA:

#1. Escribe un programa en Python para encontrar los elementos duplicados de una lista,
# añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los
# elementos únicos.
#2. Escribe un programa en Python para unir dos listas y ordenarlas en orden ascendente.
#3. Escribe un script que encuentre el segundo número más grande de una lista.
#4. Crea un script que cuente el número de elementos más grandes que un determinado número
#dado por el usuario (supón una lista numérica).
#5. Crea un script dado un número introducido por el usuario o determinado al inicio del
#programa, realice la suma de aquellos números que sean divisibles por este.
#6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto
#que es inferior al número introducido o determinado al inicio del programa.
#7. Crea un script que extraiga los elementos comunes entre dos listas.
#8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista
#(P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2)
#9. Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo
#números positivos de la lista original.
#10. Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de
#los strings de la lista original.
#11. Crea un programa que dada una lista de strings, devuelva otra lista con los strings en
#mayúscula. 

# <!-- ################################################################ --¡>

#1. Escribe un programa en Python para encontrar los elementos duplicados de una lista,
# añadirlos a una nueva lista y borrarlos de la lista. Después imprime una lista con tan solo los
# elementos únicos.


# Ejemplo de uso
#lista_original = [1, 2, 3, 4, 2, 5, 6, 3, 4, 7, 8, 1]
#print("Lista original:", lista_original)

#def encontrar_y_eliminar_duplicados(lista):
    #elementos_set = set()
    #duplicados = []

    # Encontrar elementos duplicados
    #for elemento in lista:
        #if elemento in elementos_set:
            #duplicados.append(elemento)
        #else:
            #elementos_set.add(elemento)
    
    # Eliminar elementos duplicados de la lista original
    #for duplicado in duplicados:
        #while duplicado in lista:
            #lista.remove(duplicado)
    
    # Imprimir la lista con elementos únicos (ya modificada)
    #print("Lista con elementos únicos:", lista)


#encontrar_y_eliminar_duplicados(lista_original)

#2. Escribe un programa en Python para unir dos listas y ordenarlas en orden ascendente.

# Ejemplo de uso
lista_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
lista_2 = [17,18,19,20,21,22,23,24,25,26,27,28,29]

#print("Primera lista: ", lista_1)
#print("Segunda lista: ", lista_2)

def unir_y_ordenar(lista_1, lista_2):
    # Concatenar las dos listas
    lista_combinada = lista_1 + lista_2
    # Ordenar la lista combinada en orden ascendente

    lista_combinada.sort()

    return lista_combinada

lista_ordenada = unir_y_ordenar(lista_1, lista_2)
#print("Lista combinada y ordenada: ", lista_ordenada)

# <!-- ################################################################ --¡>

#3. Escribe un script que encuentre el segundo número más grande de una lista.
def encontrar_segundo_más_grande(lista):
    return sorted(set(lista))[-2] if len(lista) >= 2 else "La lista debe tener al menos dos elementos"

# Ejemplo de uso
lista = [17,18,19,20,21,22,23,24,25,26,27,28,29]
#print("El segundo número más grande es: ", encontrar_segundo_más_grande(lista))

# <!-- ################################################################ --¡>

#4. Crea un script que cuente el número de elementos más grandes que un determinado número
#dado por el usuario (supón una lista numérica).

def contar_elementos_más_grandes(lista, número):
    return sum(1 for elemento in lista if elemento > número)

# Ejemplo de uso
lista_númerica = [5,8,2,10,3,7,1]
#numero_usuario = int(input("Ingrese un número para contar los elementos más grandes que él: "))

#cantidad_elementos = contar_elementos_más_grandes(lista_númerica, numero_usuario)
#print(f"En la lista {lista_númerica}, hay {cantidad_elementos} elementos más grandes que {numero_usuario}.")

# <!-- ################################################################ --¡>

#5. Crea un script dado un número introducido por el usuario o determinado al inicio del
#programa, realice la suma de aquellos números que sean divisibles por este.

def suma_divisibles(lista, divisor):
    return sum(numero for numero in lista if numero % divisor == 0)

# Ejemplo de uso
lista_numeros = [2,63,68,8,3,9,13,68]
#divisor = int(input("Ingrese un número divisor para realizar la suma: "))

#result = suma_divisibles(lista_numeros, divisor)
#print(f"La suma de los números en la lista son divisibles por {divisor} es: {result}")

# <!-- ################################################################ --¡>

#6. Escribe un script que pida un número al usuario y dada una lista encuentre el número más alto
#que es inferior al número introducido o determinado al inicio del programa.

#def encontrar_más_alto_inferior(lista, numero):
#    inferiores = [n for n in lista if n < numero]
#    return max(inferiores) if inferiores else None

# Ejemplo de uso
#lista_numeros = [3, 5, 9, 12, 15, 18, 20, 25]
#numeros_usuario = int(input("Ingrese un número: "))

#resultado = encontrar_más_alto_inferior(lista_numeros, numeros_usuario)
#if resultado is not None:
#    print(f"El número más alto en la lista que es inferior a {numeros_usuario} es: {resultado}")
#else:
#    print(f"No hay números en la lista que sean inferiores a {numeros_usuario}.")

# <!-- ################################################################ --¡>

#7. Crea un script que extraiga los elementos comunes entre dos listas.

# Ejemplo de listas
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [4, 5, 6, 7, 8, 9, 5]


#def elementos_comunes(lista1, lista2):
#    return list(set(lista1) & set(lista2))


#print("Elementos comunes: ", elementos_comunes(lista1, lista2))

# <!-- ################################################################ --¡>

#8. Crea un script que cuente el número de apariciones de un elemento de una lista en dicha lista
#(P.e. en la lista lista=[23, 65, 23] el número de apariciones de 23 es 2)

# Ejemplo de lista
#example = [23, 65, 23, 89, 23, 42, 65, 23, 88, 88, 88]

# Pedir al usuario el elemento a contar
#element = int(input("Ingrese el elemento a contar en la lista: "))

# Contar el número de apariciones del elemento en la lista
#numero_apariciones = example.count(element)

# Mostrar el resultado
#print(f"El número de apariciones de {element} en la lista es: {numero_apariciones}")

# <!-- ################################################################ --¡>

#9. Escribe un programa que lea una lista de enteros y cree una nueva lista que contenga solo
# números positivos de la lista original.

#def filtrar_positivos(lista):
   # return [num for num in lista if num > 0]

# Ejemplo de uso
#lista_original = [23, -65, 42, -10, 0, 15, -7, 88, -88]
#nueva_lista = filtrar_positivos(lista_original)

#print(f"Lista original: {lista_original}")
#print(f"Lista de números positivos: {nueva_lista}")

# <!-- ################################################################ --¡>

#10. Crea un script que tome una lista de strings y cree una nueva lista que contenga el tamaño de
#los strings de la lista original.

#def tamaños_strings(lista):
#    return [len(h) for h in lista]

# Ejemplo de uso
#lista_strings = ["hola","mundo", "python", "programción"]
#nueva_lista = tamaños_strings(lista_strings)

#print(f"Lista original: {lista_strings}")
#print(f"Tamaños de los strings: {nueva_lista}")

# <!-- ################################################################ --¡>

#11. Crea un programa que dada una lista de strings, devuelva otra lista con los strings en
#mayúscula. 


def Pasar_A_Mayúsculas(example):
    return [s.upper() for s in example]

# Ejemplo de uso
lista_strings = ["hola", "mundo", "python", "programación"]
nueva_lista = Pasar_A_Mayúsculas(lista_strings)

print(f"Lista oroginal: {lista_strings}")
print(f"Lista en mayúsculas: {nueva_lista}")

# <!-- ################################################################ --¡>
