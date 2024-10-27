#NUMEROS PRIMOS 2:

# Dado una lista de números enteros, escribe un script en Python que devuelva una nueva lista con
# los números primos de la lista original. Además, el script debe devolver el número total de
# números primos encontrados y la suma de los números primos encontrados

def es_primo(n):
    # Un número primo es mayor que 1 y no divisible por ningún número entre 2 y la raíz cuadrada de n
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True

def filtar_primos(lista):
    # Filtrar números primos de la lista original
    primos = [num for num in lista if es_primo(num)]

    # Contar los números primos
    total_primos = len(primos)

    # Sumar los números primos
    suma_primos = sum(primos)
    return primos, total_primos, suma_primos

# Lista de números
Z_matemáticas = [0,1,2,3,4,5,6,7,8,9]

# Llamar a la función filtrar_primos con la lista de números
primos, total_primos, suma_primos = filtar_primos(Z_matemáticas)

# Imprimir los resultados
print("Números primos: ", primos)
print("Total de números primos: ", total_primos)
print("Suma de los números primos: ", suma_primos)

