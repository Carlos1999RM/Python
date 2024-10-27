# Definir los nombres de usuarios válidos
usuarios_validos = ["Carlos", "Laura", "Alonso"]
# Pedir al usuario que ingrese su nombre
nombre_usuario = input("Por favor, ingresa tu nombre: ")

# Convertir el nombre a minúsculas para hacer la comparación más sencilla
nombre_usuario = nombre_usuario.strip().capitalize() # Capitalizar la primera letra y convertir a minúsculas el resto
# Verificar si el nombre está en lista de usuarios válidos
if nombre_usuario in usuarios_validos:
    print(f"Bienvenido/a {nombre_usuario}")
else:
    print("¡Hola, Bienvenido!. ")
