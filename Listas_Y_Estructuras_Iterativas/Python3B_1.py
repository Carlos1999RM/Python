#PALABRAS PROHIBIDAS:

#Define una lista de 5 palabras aleatorias y una lista de letras prohibidas que contenga tres letras.
#Filtra las palabras en tu lista original crea una nueva lista de palabras filtradas que solo contenga
#aquellas palabras que no tienen ninguna letra prohibida.

# Lista de palabras
lista = ["hungría", "polonia", "croacia", "eslovaquia", "españa", 'bulgaria', 'portugal', 'finlandia']

# Lista de letras prohibidas
forbidden_letters = ['d', 'm', 'u']

# Filtrar palabras que no contienen letras prohibidas
filters_words = [word for word in lista if not any(letter in word for letter in forbidden_letters)]

print(filters_words)