#Escribe un programa que pida al usuario dos números enteros y muestre por pantalla los 
#números de entrada, el cociente y el resto

#<!------------------------------------------------------------------->
### Pedir al usuario dos números enteros ###
num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa otro número entero: "))

## Calcular el cociente y el resto
cociente = num1 // num2
resto = num1 % num2
# Mostrar por pantalla números de estrada, cociente y resto
print("Los números de entrada son: ", num1, "y", num2)
print("El cociente es: ", cociente)
print("El resto es: ", resto)