# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el
# divisor es cero el programa debe mostrar un error.

# Pedir al usuario que ingrese dos números

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Verificar si el divisor es cero antes de la división
if numero2 == 0:
    print("Error: No se puede dividir entre cero.")
else:
    # Realizar la división si el dividor no es cero
    resultado = numero1 / numero2
    print(f"La división de {numero1} entre {numero2} es igual a: {resultado}"+ ".")