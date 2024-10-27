
# Array original
#array_files_columns = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,])

# Cambiar la forma del array a 3 filas y 4 columnas
#array_reshaped = array_files_columns.reshape(3,3)

#print("Array con 3 filas y 3 columnas:\n "+ f"{array_reshaped}")

# Crea una matriz identidad
#matriz = np.array([[1, 2, 3], 
                   #[4, 5, 6], 
                   #[7, 8, 9]])
# print("Matriz 3x3:\n" , matriz)

# 4. concatena ambas estructuras horizontalmente y verticalmente
# Cambiar la forma del array unidimensional a una matriz compatible para la concatenación
#array_files_columns_reshaped = array_files_columns.reshape(3,3)

# Concatenar horizontalmente (por columnas)
#concatenado_horizontal = np.hstack((array_files_columns_reshaped, matriz))

#print("Concatenado horizontalmente:\n", concatenado_horizontal)
# Concatenar verticalmente (por filas)
#concatenado_vertical = np.vstack((array_files_columns_reshaped, matriz))

#print("\nConcatenado verticalmente:\n", concatenado_vertical)

###---<!###################################################################################---¡>###

#EJERCICIOS HOJA 4 
#TEMA: USO DE ARRAYS
#OBJETIVO: FAMILIARIZACIÓN CON LA CREACION DE ARRAYS CON 
#NUMPY Y SUS MÉTODOS ASOCIADOS
#EJERCICIOS 4B 

#CALCULO DE NOTAS FINALES 
#Supongamos que tienes un conjunto de calificaciones de un grupo de estudiantes en un 
#curso. Cada estudiante tiene cuatro calificaciones: dos exámenes, un trabajo final y una 
#participación en clase. Quieres calcular la nota final de cada estudiante, donde los 
#exámenes valen un 30% cada uno, el trabajo final vale un 30% y la participación en clase 
# un 10%. Para ello, puedes usar NumPy para crear un array de 4 columnas y n filas, 
#donde n es el número de estudiantes. Cada columna representa una de las calificaciones 
#y cada fila representa un estudiante. Luego, puedes usar operaciones de NumPy para 
#calcular la nota final de cada estudiante y almacenarla en un nuevo array de una sola 
#columna.

# Calificaciones de los estudiantes
#calificacones = np.array([
    #[85, 90, 88, 92],  # Estudiante 1
   # [78, 85, 80, 85],  # Estudiante 2
   # [92, 88, 94, 90]   # Estudiante 3
#])

# Pesos para cada tipo de evaluación
#pesos = np.array([0.30, 0.30, 0.30, 0.10])

# Calcular las notas finales
#notas_finales = np.dot(calificacones, pesos)

# Mostrar las notas finales
#print("Notas finales de los estudiantes:", notas_finales)

###---<!###################################################################################---¡>###

#ANALISIS DE DATOS - VENTAS POR MES 

#Supongamos que tienes un conjunto de datos de ventas de una tienda durante un año. 
#Cada fila representa una venta y tiene tres columnas: la fecha de la venta, el monto de la 
#venta y la categoría de producto vendido (por ejemplo, electrónicos, ropa, alimentos, 
#etc.). Quieres analizar estos datos para determinar cuánto fue el monto total de ventas en 
#cada mes. Para ello, puedes usar NumPy para cargar los datos en un array de 3 
#columnas y n filas, donde n es el número de ventas. Luego, puedes usar operaciones de 
#NumPy para filtrar los datos por mes y sumar los montos de venta correspondientes. 

#(Pista 1) Tu array de entrada puede tener un a forma de este tipo:            

#(Pista 2: puedes cambiar el tipo de dato del array de string a entero usando 
#array[:,i].astype(int) ) 
import numpy as np

import pandas as pd

# Datos de ventas
datos = {
    'fecha': ["2023-01-15", "2023-01-20", "2023-02-10", "2023-02-15", "2023-03-05"],
    'monto': [150, 200, 300, 250, 100],
    'categoria': ["Electrónicos", "Ropa", "Alimentos", "Electrónicos", "Ropa"]
}

# Crear DataFrame
df = pd.DataFrame(datos)

# Convertir la columna de fechas a formato de fecha
df['fecha'] = pd.to_dateframe(df['fecha'])

# Extraer el año y el mes
df['año_mes'] = df['fecha'].dt.to_period('M')

# Agrupar por año y mes, y sumar los montos de venta
ventas_mensuales = df.groupby('año_mes')['monto'].sum().reset_index()

# Convertir el resultado a un array de NumPy
ventas_mensuales_array = ventas_mensuales.to_numpy()

# Mostrar los resultados
print(ventas_mensuales)
print(ventas_mensuales_array)