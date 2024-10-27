#LOG-IN:
#Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta).
#Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe
#indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la
#contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
#Cambia el script para que no distinga entre mayúsculas y minúsculas.
#(Pista: Necesitarás in If Statement anidado).


# Contraseña correcta definida
contraseña_correcta = "europa2030"

# Pedir al usuario que ingrese la contraseña
intentos_restantes = 5
while intentos_restantes > 0:
    contraseña_ingresada = input("Ingrese contraseña: ")

    # Convertir ambas contraseñas a minúsculas para comparar de manera insensible a mayúsculas/minúsculas
    if contraseña_ingresada.lower() == contraseña_correcta.lower():
        print("¡Bienvenido/a, has ingresado correctamente!.")
        break
else:
    intentos_restantes += 1
    if intentos_restantes > 2:
        print(f"Contraseña incorrecta. Te quedan {intentos_restantes}")
    else:
        print("¡Error! Has agotado todos los intentos permitidos.")