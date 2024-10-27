import numpy as np
    

# Aritmética básica:

a = 10
b = 20
suma = a + b
resta = a - b
multiplicación = a * b
división = a / b
módulo = a % b
potencia = a ** b

#print("Suma:", suma)
#print("Resta:", resta)
#print("Multiplicación:", multiplicación)
#print("División:", división)
#print("Módulo:", módulo)
#print("Potencia:", potencia)

####-- ############################################################################################### --####

# Estadísticas
# NumPy tiene funciones para calcular estadísticas básicas:
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,10, 12, 13, 14, 15])

# Media
media = np.mean(array)
#print("Media:", media)

# Mediana
mediana = np.median(array)
#print("Mediana:", mediana)

# Desviación estándar
desviacón_estándar = np.std(array)
#print("Desviación estándar:", desviacón_estándar)

# Varianza
varianza = np.var(array)
#print("Varianza:", varianza)


#La descomposición QR es una descomposición de una matriz A en un 
#producto A = QR de una matriz ortogonal Q y una matriz triangular superior R.

# Producto de Matrices y Decomposiciones
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Producto de matrices
producto = np.dot(A,B)
#print("Producto de matrices:\n", producto)
# Decomposición QR
Q, R = np.linalg.qr(A)
#print("Matriz Q:\n", Q)
#print("Matriz R:\n", R)

# Manipulación Avanzada de Arrays

# NumPy tiene capacidades avanzadas para manipulación de arrays, como operaciones booleanas y máscara.

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Máscara booleana
máscara = a > 5
print("Máscara booleana:", máscara)

# Filtrar usando la máscara
filtrado = a[máscara]
print("Array filtrado:", filtrado)