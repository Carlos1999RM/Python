
# 3. Crea un script que pida al usuario una palabra y luego muestre por pantalla una a una las letras
# de la palabra introducida empezando por la última.

def mostrar_palabra_reversed(word):
    # Iterar sobre la palabra en reversa
    for word in reversed(word):
        print(word)

# Solicitar al usuario una palabra
users_word = input("Introduce una palabra mi reina: ")

# Llamar a la función para mostrar las letras en reversa
mostrar_palabra_reversed(users_word)