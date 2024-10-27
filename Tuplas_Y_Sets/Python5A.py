# 1. Crea una tupla con tres elementos y imprime por pantalla cada uno de ellos en una nueva linea.
import sys
tupla_1 = (25, "Carlos", "Jerez de la frontera")
#print(tupla_1)

##<####################################################################################################################>##
# 2. Crea una lista con tres elementos e intenta modificarla. Haz lo mismo con la tupla. ¿Cuáles son las diferencias? 
lista = [25, "Carlos", "Jerez de la frontera"]
#print(lista)

##<####################################################################################################################>##
# 3. Crea una tupla de enteros y devuelve la suma de los elementos.
# Crear una tupla con enteros
tupla_enteros = (20, 50)
# Sumar los elementos de la tupla
suma = sum(tupla_enteros)
# Imprimir la suma
#print(suma)

##<####################################################################################################################>##

# 4. Crea un script que dada una tupla que contiene strings cree una nueva tupla con el primer caracter de cada string.
String_tupla = ("carlos", "richarte", "moreno")

# Crear una nueva tupla con el primer carácter de cada string
new_tupla = tuple(s[0] for s in String_tupla)

# Imprimir la nueva tupla
#print(f"Nueva tupla con el primer carácter de cada string: {String_tupla}")

##<####################################################################################################################>##

# 5. Crea un script que dada una tupla de números devuelva el producto de todos los números pares. 
# Importar la función reduce del módulo functools
from functools import reduce

# Definir una función para la multiplicación
def multiplicación(a,b):
    return a * b

# Crear una tupla con números
tupla_producto = (2, 6, 18, 36, 39, 22, 57, 66)

# Filtrar los números pares de la tupla
numeros_pares = tuple(num for num in tupla_producto if num % 2 == 0)

# Verificar si hay números pares en la tupla
if numeros_pares:
    # Multiplicar los números pares usando reduce y la función multiplicar
    producto = reduce(multiplicación, numeros_pares)
else:
    # Si no hay números pares, el producto es 1 (neutro multiplicativo)
    producto = 1

# Imprimir el resultado
#print(f"El producto de todos los números pares de la tupla es: {producto}")

##<####################################################################################################################>##

# 6. Crea un script que dada una tupla de números, devuelva la tupla con los numeros ordenados en orden descendente.
def ordenar_tupla_descendente(tupla):
    return tuple(sorted(tupla, reverse=True))

# Ejemplo de uso
tupla_descendente = (10, 20, 30, 40, 50 , 60, 70, 80 , 90, 100)
devolver_inverso = ordenar_tupla_descendente(tupla_descendente)
#print("Tupla original: ", tupla_descendente)
#print("Tupla ordenada: ", devolver_inverso)

##<####################################################################################################################>##
# 7. Crea un script que dada una tupla con números enteros repetidos, elimine los duplicados. (Puedes usar sets).
def eliminar_duplicados(tupla):
    return tuple(set(tupla))


# Ejemplo de uso
tupla_original = (1, 5, 1, 3, 8, 3, 1, 2, 5, 8, 2)
tupla_sin_duplicados = eliminar_duplicados(tupla_original)
#print("Tupla original:", tupla_original)
#print("Tupla sin duplicados:", tupla_sin_duplicados)

##<####################################################################################################################>##
# 8. Crea un script que dada una tupla y un numero entero, devuelve verdadero si el numero se encuentra en la 
# tupla y falso en el caso contrario. 
def esta_en_tupla(tupla, numero):
    return numero in tupla

# Ejemplo de uso
tupla_principal = (5, 3, 8, 1, 2)
numero_a_buscar = 3
resultado = esta_en_tupla(tupla_principal, numero_a_buscar)
#print("¿Está el número en la tupla?", resultado)

##<####################################################################################################################>##
# 9. Crea un script que dadas dos tuplas cree una tupla resultante de la union de ambas. 
tupla_0 = (25,23,25)
tupla_01 = ('Carlos','Guillermo', 'Joaquín')

tupla_combinada = tuple(zip(tupla_0, tupla_01))
#print("Tabla combinada: ",tupla_combinada)

##<####################################################################################################################>##
# 10.  Crea un script que dada una tupla de números devuelva e máximo y el mínimo.
def obtener_máximo_mínimo(tupla):
    # Obtener el máximo y el mínimo de la tupla
    máximo = max(tupla)
    mínimo = min(tupla)
    return máximo, mínimo

# Ejemplo de uso
tupla_números = (1, 100, 50, 20)
máximo, mínimo = obtener_máximo_mínimo(tupla_números)
#print("Número más alto: ", máximo)
#print("Número más bajo: ", mínimo)

##<####################################################################################################################>##
# 11.  Crea un script que dada una tupla con strings devuelva el string más largo y el más corto. 
# (Prueba añadiendo key=len a las funciones max y min).
def find_longest_and_shortest(strings):
    if not strings:
        return None, None
    longest = max(strings, key=len)
    shortest = min(strings, key=len)
    return longest, shortest

# Ejemplo de uso
String_tupla = ("apple", "banana", "cherry", "date", "elderberry", "fig", "grape")
longest, shortest = find_longest_and_shortest(String_tupla)
#print(f"Longest string: {longest}")
#print(f"Shortest string: {shortest}")

##<####################################################################################################################>##
# 12.  Crea un script que dada una tupla devuelva el contenido en orden revertido. 
def reverse_tuple(a):
    return a[::-1]

# Ejemplo de uso
example_tuple = (1999, 400, 1346, 1362, 1758, 1936)
reversed_tuple = reverse_tuple(example_tuple)
#print(f"Original tuple: ", example_tuple)
#print(f"Reverse tuple: ", reversed_tuple)

##<####################################################################################################################>##
# 13.  Crea un script que dada una tupla de tuplas, donde cada tupla interna contiene dos 
# elementos, devuelva una nueva tupla en la que cada elemento sea la suma de los dos 
# elementos de la tupla interna correspondiente. 
def sum_inner_tuples(tuples):
    return tuple(a + b for a, b in tuples)

# Ejemplo de uso
examples_tuples = ((1,2), (3,4), (5,6),(7,8))
summend_tuples = sum_inner_tuples(examples_tuples)
#print(f"Original tuple of tuples: {example_tuple}")
#print(f"Summed tuple: {summend_tuples}")


##<####################################################################################################################>##
##<####################################################################################################################>##
# TRBAJANDO CON SETS:  
# 14. Crea un set y elimina uno de sus elementos.
my_set = {0,1,2,3,4,5,6}
#my_set.add(7)
my_set.remove(6)
#print(my_set)

##<####################################################################################################################>##
# 15. Crea un set vacío.
my_set = set()
#print(my_set)
##<####################################################################################################################>##

# 16. Crea dos sets y encuentra su union, su intersección y su diferencia. 
conjunto_1 = {1,2,3}
conjunto_2 = {3,4,5}

# Unión
union = conjunto_1 | conjunto_2 # {1,2,3,4,5,6}
union = conjunto_1.union(conjunto_2)
#print(union)

# Intersección
intersection = conjunto_1 & conjunto_2 # {3}
intersection = conjunto_1.intersection(conjunto_2)
#print("Número repetido: "+f"{intersection}")

# Diferencia
diferencia = conjunto_1 - conjunto_2 # {1, 2}
diferencia = conjunto_1.difference(conjunto_2)
#print(diferencia)

##<####################################################################################################################>##
# 17. Crea un script que dados dos sets cree uno nuevo que contenga solo los elementos comunes de ambos. 
set_1 = {1,2,3,4,5,6,7,8,9,10}
set_2 = {1,12,3,44,5,68,77,8,99,110}

comunes = set_1 & set_2
comunes = set_1.intersection(set_2)
#print(f"Números comúnes: ", comunes)

##<####################################################################################################################>##
# 18. Crea un script que dado un set con números devuelva el numero máximo y mínimo.
set_números = {10,20,30,40,50}

# Encontrar el valor máximo
máximo = max(set_números)
#print(f"El valor máximo es: ", máximo)

# Encontrar el valor mínimo
mínimo = min(set_números)
#print(f"El valor mínimo es: ", mínimo)

##<####################################################################################################################>##
# 19. Crea un script que dados dos sets cree uno nuevo solo con los elementos únicos de cada uno de los sets. 
def elementos_únicos(set1, set2):
    return set1.symmetric_difference(set2)

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {1,12,34,5,6,9,0,10,4}

sets_únicos = elementos_únicos(set1, set2)

#print("Elementos únicos:", sets_únicos)

##<####################################################################################################################>##
# 20. Crea un set con colores y comprueba si cierto color se encuentra en el set.
# Definir el conjunto de colores
colors = {"rojo", "verde", "azul", "amarillo"}


# Definir el color a comprobar
colors_comprobar = "morado"


# Comprobar si el color está en el conjunto
#if colors_comprobar in colors:
    #print(f"El color {colors_comprobar} se encuentra en el conjunto.")
#else:
    #print(f"El color {colors_comprobar} no se encuentra en el conjunto.")
    
##<####################################################################################################################>##
# 21. Crea un script que dados dos sets cree un nuevo set con los elementos que están en 
# el primer set pero no en el segundo. 
conjunto = {200,300,400,500,600}
conjunto_0 = {400,600,700,800,200}

# Calculamos la diferencia entre set1 y set2
result = conjunto - conjunto_0

# Mostramos el resultado
#print("Elemento en conjunto pero no en conjunto_0:", result)

##<####################################################################################################################>##
# 22. Crea un script que dado un set de enteros devuelva el producto de todos los números dentro del set.
# Definimos un conjunto de enteros
entero_set = {1,2,3,4,5,6}

# Calculamos el producto de todos los números en el set
producto = 1
for num in entero_set:
    producto *= num

# Mostramos el resultado
print("El producto de todos los números en el set es: ", producto)