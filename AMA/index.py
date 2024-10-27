#Usando range()
#El uso de range() es común para iterar un número específico de veces.

#for iteración in range(0, 100, 10): # Esto iterará desde 0 hasta 4
    #print(iteración)

#Uso de else con while
#El bloque else se ejecuta si el bucle se completa sin interrupciones (sin break).
#contador = 0
#while contador < 5:
    #print(contador)
    #contador += 1
#else:
    #print("Bucle completado")

#for contador in range(5):
#    print(contador)
#else:
#    print("Bucle completado")

#response = input("¿Crees que el imperio Español es el mejor imperio? (si/no):").strip().lower()

# Evalúa la respuesta del usuario
#if response == 'si':
    #the_spanish_empire_is_the_best_empire = True
# response == 'no':
    #the_spanish_empire_is_the_best_empire = False
#else:
    #print("Respuesta no válida, pro favor responde con 'si' o 'no'.")
    #exit() # Salir si la respuesta no es válida


#the_spanish_empire_is_the_best_empire = True

# Condicional basado en the_spanish_empire_is_the_best_empire
#if the_spanish_empire_is_the_best_empire:
    #print("Gibraltar is Spanish")
#else:
    #print("The british are thief people.")

import array as arr
import numpy as np

# Array de números
#array = list(range(161))

#print("Array de numeros:",array[::])

inventario = np.array(["lavadora", "freidora", "satén", "batidora", "Lavavajillas"])
precio = np.array([400, 120, 50, 75, 300])
print(type(inventario[precio >= 300]))

