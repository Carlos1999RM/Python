
#MAYUSCULA O MINUSCULA (BONUS*):

#Permite que el usuario introduzca una letra (del alfabeto latino) como input. Comprueba si esta es
#una mayúscula o una minúscula.
#*Los ejercicios bonus no se resolverán directamente en clase si no que están pensados para que
#los alumnos los discutan por el chat de Discord y compartan sus soluciones. Las soluciones
#compartidas de los alumnos se subirán en un archivo a la academia.

# Solicitar la letra al usuario
letra_usuario = input("Introduce una letra del alfabeto latino: ")

# Función para comprobar si una letra es mayúscula o minúscula
def comprobar_letra(letra):
    if letra.isalpha() and len(letra) == 1: # Verifica si es una letra del alfabeto y si es un solo carácter
        if letra.isupper():
            return "La letra es una mayúscula."
        elif letra.islower():
            return "La letra es una minúscula."
        else:
            return "Por favor, introduce una letra del alfabeto latino: "
        

# Comprobar y mostrar el resultado
resultado = comprobar_letra(letra_usuario)
print(resultado)