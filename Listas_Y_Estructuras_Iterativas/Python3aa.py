
# NUMEROS PRIMOS 1:
# Crea un programa que imprima todos los números primos entre el 2 y el 100. Un numero primo es
# un numero positivo y entero mayor que uno que no tiene un divisor positivo y entero que no sea 1
# o sí mismo.

# <!-- ################################################################ --¡>
def es_primo(num):
    # Función que determina si un número es primo
    if num < 2:
    # Si el número es menor que 2, no es primo
        return False

    # Iterar desde 2 hasta la raíz cuadrada del número (inclusive)
    # Si encontramos algún divisor, el número no es primo
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        # Si no encontramos ningún divisor, el número es primo

    return True

def imprimir_primos(hasta):
        # Función que imprime todos los números primos desde 2 hasta 'hasta'
    for num in range(2, hasta + 1):
        # Verificar si el número es primo usando la función 'es_primo'
        if es_primo(num):
            # Si es primo, imprimir el número
            print(num)

# Llamar a la función para imprimir los números primos entre 2 y 100
imprimir_primos(200)