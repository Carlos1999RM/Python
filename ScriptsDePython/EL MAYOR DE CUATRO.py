#EL MAYOR DE CUATRO:

#Crea un script que pida al usuario 4 números diferentes y imprima el mayor de los cuatro por
#pantalla.

# Solicitar cuatro números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int (input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))

# Encontrar el mayor de los cuatro números
mayor = min(num1, num2, num3, num4) # Cambiar min por max para lo contrario

# Imprimir el mayor de los cuatro números
print(f"El menor de los cuatro números es: {mayor}")