import numpy as np

# Crear un array de una dimensión
#array_1d = np.array([1,2,3,4,5])
# Crear un array de dos dimensiones (matriz)
# = np.array([[4,4,3], [4,5,6]]) # añadir [] para agrupar ha ambos.
# Acceder a elementos del array
#print("Primer elemento del array 1D: ", array_1d[0]) # 1
#print("Elemento (0, 1) del array 2D: ", array_2d[0, 1]) # 2
# Operaciones aritméticas
#array_sumado = array_1d + 2
#array_multiplicado = array_1d * 2

#print("Array sumado con 2: ", array_sumado) #[3,4,5,6,7]
#print("Array multiplicado por 2: ", array_multiplicado) #[2,4,6,8,10]
# Funciones matemáticas
#suma_total = np.sum(array_1d)
#average = np.mean(array_1d)

#print("Suma total del array 1D: " , suma_total) # 15
#print("Promedio del array 1D: ", average)

#import numpy as np
#("Version of Numpy:",np.__version__)

# Array bidimensional
#array_1 = np.array([[1,2,3], [4,5,6]], dtype = np.int8)
#print("array_1 shape: ", array_1.shape, "dim", array_1.ndim)
#print(array_1)
#array_2 = array_1.reshape(6)
#print("array_2 shape: ", array_2.shape, "dim", array_2.ndim)
#print(array_2)

#my_array = np.arange(0,12000,100)
#print(my_array)
#(type(my_array))
#array_vacio = np.empty((1,10))
#print(array_vacio)

#a = np.zeros((3, 3), dtype = np.int64)
#a[:] = 2
#print(a)

###---<!###################################################################################¡>---###

#b = np.arange(1,10).reshape((3,3))
#b[:] = 2
#print(b)

###---<!###################################################################################¡>---###
#a = np.zeros((3,3), dtype = np.int64)
#a[:] = 2
#a.fill(8)
#print(a)

###---<!###################################################################################¡>---###

#b = np.arange(1,10).reshape((3,3))
# = b.mean() # Puedes cambiar el mean por min() o max().
#print(b)
#print(mean_array)

###---<!###################################################################################¡>---###
#b = np.arange(1,10).reshape((3,3))
#array_plano = b.reshape(b.size) #reshape() + size
#print(b)
#print(array_plano)

#b = np.arange(1,10).reshape((3,3))
#array_plano = b.flatten() #flatten()
#print(b)
#print(array_plano)

#b = np.arange(1,10).reshape((3,3))
#array_plano = b.ravel() #ravel()
#print(b)
#print(array_plano)

###---<!###################################################################################

#import numpy as np
#print("Version of Numpy:",np.__version__)

'''EJERCICIOS HOJA 4'''
'''ARRAYS 1D PARTE 1:'''
# 1. Crea un array_1 lleno ceros con una longitud de 8 elementos.
array_1 = np.zeros([8], dtype=int)

# 2. Haz que todos los elementos de este array sean igual a 2
array_1[[0,1,2,3,4,5,6,7]] = 2
#print(array_1)

# 3. Crea un array_2 que contenga todos los números pares del 1 al 10.
array_2 = np.arange(0,12,2)
#print(array_2)

# 4. Suma todos los elementos del array_2 usando un bucle y después usando un método
# de numpy. Compara los resultados

# Create a NumPy array
arr_2 = np.array([0,12,2])

# Initialize a variable to hold the sum
total_sum = 0

# Iterate over each element in the array and add it to total_sum
for num in arr_2:
    total_sum += num

#print("The sum of the array elements is:",total_sum)

###---<!###################################################################################
'''sumar con método numpy'''

# Use NumPy's sum function
total_sum = np.sum(arr_2)

#print("The sum of the array elements is:",total_sum)

# 5. Revierte array_2 y guárdalo en una variable independiente.
# Create a 1D NumPy array
arr_2 = np.array([1,2,3,4,5,6,7,8,9,10])

# Reverse the array and store it in another variable
reversed_arr_2 = arr_2[::-1]

#print("Original array: ", arr_2)
#print("Reversed array: ", reversed_arr_2)

# 6. Encuentra los elementos comunes entre array_1 y array_2 y entre array_2 y
# array_2_revertido
# (Pista: Investiga el uso de intersect1d() de numpy)

interseccion = np.intersect1d(np.intersect1d(array_1, array_2), reversed_arr_2)
#print("Números o números común:",interseccion)

###---<!###################################################################################

# 7. Crea un arrays lleno de 1s con una longitud dada por el usuario
# Solicitar al usuario la longitud del array
#longitud = int(input("Introduce la longitud del array: "))

# Crear un array de unos con la longitud especificada

#array = np.ones(longitud, dtype=int)

#print("Array creado: ", array)

###---<!###################################################################################
'''ARRAYS 1D PARTE 2:'''
# 1. Crea un array con 15 números enteros aleatorios entre 1 y 100
array_quince_números = np.random.randint(low=1, high=101, size=15)
#print(array__quince_números)

# 2. Multiplica todos los elementos del array usando un bucle y después usando un
# método de numpy. Compara los resultados

multiplicar = 3
resultado = array_quince_números * multiplicar

#print("Matriz original:",array__quince_números)
#print("Matriz multiplicada por",multiplicar,":",resultado)


# 3. Crea otro array con 15 números decimales aleatorios entre 0 y 1
array_con_decímales = np.random.uniform(0,1,15)
#print(array_con_decímales)

###---<!###################################################################################

#4. Suma los elementos de ambos arrays elementos por elemento. Resuélvelo usando un
#operador y después con una función de numpy
#(Pista: busca en google que función de numpy hace esto)

# Sumar los arrays elemento a elemento
resultado = array_quince_números + array_con_decímales

# Sumar los arrays elemento a elemento usando np.add
resultado = np.add(array_quince_números, array_con_decímales)

#print("Primer array:", array__quince_números)
#print("Segundo array:", array_con_decímales)
#print("Resultado de la suma elemento a elemento:", resultado)

###---<!###################################################################################

# 5. Ahora réstalos. Resuélvelo usando un operador y después con una función de numpy
# (Pista: busca en google que función de numpy hace esto)

# Restar los arrays elemento a elemento
resultado = array_quince_números - array_con_decímales

# Restar los arrays elemento a elemento usando np.subtract
resultado = np.subtract(array_quince_números, array_con_decímales)

#print("Primer array:", array__quince_números)
#print("Segundo array:", array_con_decímales)
#print("Resta:",resultado)

###---<!###################################################################################

# 6. Haz lo mismo que en la resta pero multiplicando

# Normal
resultado = array_quince_números * array_con_decímales

# Con numpy
resultado = np.multiply(array_quince_números, array_con_decímales)

#print("Primer array:", array__quince_números)
#print("Segundo array:", array_con_decímales)
#print("Multiplicación:",resultado)

# 7. Encuentra el valor más alto del primer array que has creado.
#print(max(array_quince_números))

###---<!###################################################################################

# 8. Calcular media de un array
resultado = np.median(array_quince_números)
#print(resultado)

# Desviación estándar
resultado = np.std(array_quince_números)
#print(resultado)


###---<!###################################################################################
many_numbers = np.random.random(size = 1000000)
ordenada = many_numbers.sort()
print(many_numbers)