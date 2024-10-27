
#MATRIZ:

#Crea un script que dada una lista de listas M (numérica), identifique si se trata de una matriz y en
#ese caso imprima dos listas correspondientes a:
#1. La fila cuyos elementos suman el máximo
#2. La columna cuyos elementos suman el máximo
#Si no se trata de una matriz devolverá dos listas vacías.
#Por ejemplo:
#M1=[[2,5,3],[6,1,8],[7,5,4]] devolverá: L1 = [7,5,4] y L2 = [2,6,9,7]
#M2 = [[4,2,3],[4,5],[6,8,2]] devolverá: L1 = [] y L2 = []
#(Nota: Definimos matriz como una lista de listas donde todas las listas internas tienen el mismo
#numero de objetos)
def procesar_matriz(M):
    # Verificar si es una matriz
    if not M or not all(len(fila) == len(M[0]) for fila in M):
        return [], []
    
    # Calcular la suma de cada fila y encontrar la fila con la suma máxima
    max_fila = max(M, key=sum)

    # Calcular la suma de cada columna y encontrar la columna con la suma máxima
    num_columnas = len(M[0])
    sumas_columnas = [sum(fila[i] for fila in M) for i in range(num_columnas)]
    max_columna_index = sumas_columnas.index(max(sumas_columnas))
    max_columna = [fila[max_columna_index] for fila in M]

    return max_fila, max_columna

# Listas
M1 = [[2, 5, 3], [6, 1, 8], [7, 5, 4]] 
M2 = [[4, 2, 3], [4, 5], [6, 8, 2]]

L1_1, L2_1 = procesar_matriz(M1)
L1_2, L2_2 = procesar_matriz(M2)

# Salida por pantalla
print("Para M1: ")
print("L1 =", L1_1)
print("L2 =", L2_1)

print("\nPara M2:")
print("L1 =", L1_2)
print("L2 =", L2_2)


#Explicación del código:

#Verificación de matriz: Se comprueba si todas las sublistas tienen la misma longitud. Si alguna sublista 
#tiene una longitud diferente, no es una matriz válida y se devuelven dos listas vacías.

#Máxima suma de filas: Se encuentra la fila cuya suma de elementos es la mayor usando max(M, key=sum).

#Máxima suma de columnas: Se calcula la suma de cada columna y se encuentra la columna con la suma máxima.

#Este script es más compacto y fácil de entender, manteniendo la funcionalidad requerida.