#SCRABBLE:

#Supongamos una lista de de caracteres llamada “palabras“ que representa una mano de
#Scrabble. Cada string contiene dos caracteres: el primer carácter es la letra de una ficha y el
#segundo el numero que representa los puntos de la ficha. Por ejemplo, el string "A5" representa la
#ficha con la letra A y un valor de 5 puntos. Crea un script que calcule el valor total de los puntos
#en una mano de scrabble. El valor total será la suma de los puntos de todas las fichas de la mano.

# Lista de Scrabble
palabras_scrabble = ["A5", "B7", "C1", "D4", "E9"]

# Calcular el valor total de los puntos en la mano
valor_total_scrabble = sum(int(token[1]) for token in palabras_scrabble)

# Imprimir el valor total
print("El valor total de los puntos en la mano de Scrabble es: ", valor_total_scrabble)