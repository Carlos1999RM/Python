# Creando función
def funcion_suma(x, y):
    suma = x + y
    return(suma)

# Solicitar los valores al usuario
x = int(input("Ingresa el primero: "))
y = float(input("Ingrese el segundo: "))

# Llamar a la función con los valores proporcionados por el usuario
result = funcion_suma(x, y)

# Imprimir el resultado
print("La suma es: ", result)