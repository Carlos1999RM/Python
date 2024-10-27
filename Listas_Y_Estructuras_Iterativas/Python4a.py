
#- 4. Crea un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
# pantalla el número de veces que aparece la letra en la frase.

# <!-- ################################################################ --¡>

def juego_una_letra_en_frase(sentence, word):
    # Contar el número de veces que aparece la letra en la frase

    return sentence.count(word)

# Solicitar al usuario una frase
users_sentence = input("Introduce una frase: ")

# Solicitar al usuario una letra
users_letter = input("Introduce una letra: ")


# Asegurarse de que el usuario introduzca solo una letra
while len(users_letter) != 1:
    users_letter = input("Por favor, introduce una sola letra: ")

# Llamar a la función para contar la letra y mostrar el resultado
numero_de_veces = juego_una_letra_en_frase(users_sentence, users_letter)
print(f"La letra '{users_letter}' aparece {numero_de_veces} veces en la frase.")