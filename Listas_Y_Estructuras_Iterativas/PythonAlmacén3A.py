#2. Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

# <!-- ################################################################ --¡>

password = "apostrofe12345A"
password_input = ""

while password_input != password:
    password_input = input("Introduzca la contraseña: ")
    if password_input != password:
        print("Invalid password, try again.")

print("Correct password, entry valid.")