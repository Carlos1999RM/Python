#EJERCICIOS HOJA 4 
import array as arr
import numpy as np
#TEMA: USO DE ARRAYS
#OBJETIVO: FAMILIARIZACIÓN CON LA CREACION DE ARRAYS CON 
#NUMPY Y SUS MÉTODOS ASOCIADOS
#EJERCICIOS 4C 

#DATOS CINEMATOGRÁFICOS 
#Supongamos que tienes un conjunto de datos de películas que contiene información 
#sobre su título, género, duración, año de lanzamiento y calificación. Quieres analizar 
#estos datos para determinar cuál es el género de película más popular, cuántas películas 
#se lanzaron en cada década y cuál es la duración promedio de cada género de película. 

#(Pista 1: Tu array de entrada puede tener la forma...) 
films = np.array([
    ['Peli 1', 'Comedia', 100, 1990, 6.3],
    ['Peli 2', 'Acción', 170, 2005, 8.7],
    ['Peli 3', 'Drama', 120, 2000, 5.5],
    ['Peli 4', 'Acción', 120, 2000, 6.9],
    ['Peli 5', 'Humor', 110, 1988, 7.7],
    ['Peli 6', 'Acción', 140, 2008, 6.3],
    ['Peli 7', 'Acción', 90, 2006, 8.2],
    ['Peli 8', 'Drama', 80, 1990, 7.5],
    ['Peli 9', 'Acción', 120, 2002, 6.5],
    ['Peli 10', 'Ciencia-ficción', 120, 2005, 6.7]
])

#(Pista 2: puede ser util investigar np.unique, np.argsort y np.count_nonzero) 
generos, counts = np.unique(films[:, 1], return_counts=True)
genero_mas_popular = generos[np.argmax(counts)]
print(f"El género más popular es: {genero_mas_popular}")

# 2. Contar la cantidad de películas lanzadas en cada década
años = films[:, 3].astype(int)
décadas = (años // 10) * 10
décadas_unicas, counts_décadas = np.unique(décadas, return_counts=True)
print('Cantidad de películas lanzadas por décadas: ')
for década, count in zip(décadas_unicas, counts_décadas):
    print(f'{década}s: {count} películas')

# 3. Calcular la duración promedio de cada género de película
duraciones = films[:, 2].astype(int)
duracion_promedio_por_genero = {}
for genero in generos:
    indices = np.where(films[:, 1] == genero)
    duracion_promedio_por_genero[genero] = duraciones[indices].mean()
print("Duración promedio por género:")
for genero, duracion_promedio in duracion_promedio_por_genero.items():
    print(f"{genero}: {duracion_promedio:.2f} minutos")