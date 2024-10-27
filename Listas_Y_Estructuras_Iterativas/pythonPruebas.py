# -- Ejemplo 1: Verificar si un número es positivo
#number = int(input("Introduce un número: "))

#if number > 10:
  #  print("Es mayor que diez")
#elif number == 0:
  #  print("Es igual a cero.")
#else:
    #print("NO ES NINGUNO.")

#Ejemplo 5: Verificar si una lista contiene un elemento específico

#list = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 0]

#if 6 in list:
   # print("El seis está en la lista.")
#elif 1 in list:
  #  print("El ocho está en lista")

#import time
#temporizador = int(input("Introduce el número de segundos del temporizador: "))

#print("Comienza el temporizador")

#for i in range(temporizador, 0, -1):
 #   print("Quedan ", i, " segundos")
   # time.sleep(1)

#print("El temporizdor ha finalizado.")

##-- BUCLE FOR --##

## Iterar sobre un diccionario

#edades = {'Carlos':25, 'Laura': 27, 'Alicia': 24}

#for nombre, edad in edades.items():
   # print(f'{nombre}' + ' tiene ' + f'{edades}' +  ' años.')



## Ejemplo con una lista y continue
#names = ['Alice', 'Alex', 'Charles', 'Anthony','Sofie']

#for name in names:
   # if name.startswith('A'):
     #   continue
   # print(name)

#my_list = [1,2,3,4,5,6,7,8,9]

#print(my_list[5])
#print(my_list[-2])

# <!-- ################################################################ --¡>

##  Inicializa una list de números  ##
#list_number = []

## Crear un bucle para ir pidiendo los números

## y añadiendo la lista

#for i in range(0, 4):
    # Pido el número
  #  number = input("Introduce un números: ")
    # lo convierto en entero
  #  number = int(number)
    # lo añado a la lista de números
 #   list_number.append(number)

# output: lista con cuatro números

# imprimo el mayor número de la lista por pantalla
#print("El número más bajo es: ", min(list_number))
# imprimir la lista ordenada
#print("Los números introducidos en orden ascendente son", sorted(list_number))

# <!-- ################################################################ --¡>

# Inicializo la lista de números
#list_number = []
#terminado = False
# Crear un bucle para ir pidiendo números
# y añadirlos a la lista
#while terminado == False:
    # pedir los números
    #numero = input("Introduce un número: ")
    # convertirlos a enteros
   #numero = int(numero)
    # añadirlos a la lista
    ##list_number.append(numero)

#if len(list_number) == 5:
      ##  terminado = True
# output: lal ista con los cuatro números enteros
# Devolver el número mayor
#print("El número más alto es: ", max(list_number))

# Devolver los números en orden ascendente
#print("Los números en orden ascenente son: ", sorted(list_number))

# <!-- ################################################################ --¡>

# lista de precios
precios = [10.99, 23.78, 34.28, 43.25, 24.23, 8.88]
precio_total = 0
precio_max = 0.0
precio_min = float('inf')
# -- bucle para recorrer en la lista
for precio in precios:
    # if statament
    # Comprobamos si el precio es más alto que el anterior
    if precio > precio_max:
        precio_max = precio
    # comprobamos si el precio más bajo que el anterior
    if precio < precio_min: 
        precio_min = precio
    # sumamos los valores de la lista
    precio_total += precio

print("El precio más alto es: " , precio_max)
print("El precio más bajo es: " , precio_min)
# --- calculamos el precio promedio

# --- imprimirlo por pantalla

