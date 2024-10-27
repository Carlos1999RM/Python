# Pedir al usuario que ingrese un número entero
number = int(input("Por favor, ingresa un número entero: "))

# Verificar si el número es par o impar
if number % 2 == 0:
    print(f"El número {number} es PAR.")
else:
    print(f"El número {number} es IMPAR")