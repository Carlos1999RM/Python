#ANALISIS DE DATOS CLIMÁTICOS 

#Supongamos que tienes un conjunto de datos de clima que contiene información sobre la 
#temperatura, la humedad y la presión atmosférica en una ciudad durante un año. Quieres 
#analizar estos datos para determinar cuál fue la temperatura promedio de cada mes, cuál 
#fue la humedad promedio y la presión atmosférica promedio durante todo el año. Para 
#ello, puedes usar NumPy para cargar los datos en un array de 3 columnas y n filas, donde 
#n es el número de mediciones. Luego, puedes usar operaciones de NumPy para filtrar los 
#datos por mes y calcular las medias de temperatura, humedad y presión atmosférica 
#correspondientes. 
#(Pista 1) Tu array de entrada podría ser algo como esto, con daros de temperatura, 
#humedad, presión y mes del año: 

import numpy as np
import pandas as pd

# Datos de clima (normalmente cargarías esto desde un archivo CSV)
datos = {
    'fecha': ["2023-01-01", "2023-01-02", "2023-02-01", "2023-02-02", "2023-03-01", "2023-03-02"],
    'temperatura': [5, 7, 6, 8, 10, 12],
    'humedad': [85, 80, 78, 75, 70, 65],
    'presion': [1012, 1011, 1009, 1010, 1008, 1007]
}

# Crear DataFrame
dataFrame = pd.DataFrame(datos)

# Convertir la columna de fechas a formato de fecha
dataFrame['fecha'] = pd.to_datetime(dataFrame['fecha'])

# Extraer el año y el mes
dataFrame['año_mes'] = dataFrame['fecha'].dt.to_period('M')

# Calcular las medias mensuales de temperatura, humedad y presión
medias_mensuales = dataFrame.groupby('año_mes').agg({
    'temperatura': 'mean',
    'humedad': 'mean',
    'presion': 'mean'
}).reset_index()

# Calcular las medias anuales de humedad y presión
medias_anual_humedad = dataFrame['humedad'].mean()
medias_anual_presion = dataFrame['presion'].mean()

# Convertir los resultados mensuales a un array de NumPy
medias_anual_array = medias_mensuales.to_numpy()

# Mostrar los resultados
print("Medias mensuales de temperatura, humedad y presión:")
print(medias_mensuales)
print("\nArray de Numpy de medias mensuales:")
print(medias_anual_array)
print("\nArray promedio anual:", medias_anual_humedad)
print("Presión atmosférica promedio anual:", medias_anual_presion)