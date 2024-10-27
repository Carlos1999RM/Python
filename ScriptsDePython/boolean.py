## Leemos los datos
##  que necesitamos
#hasPagado = input()
#precio = float(input())

## condional IF anidado
#if hasPagado == "false":
   # print("No has pagado aún")
   # if precio <= 20:
     #   print("Tienes que paga menos de 20 euros")
   # else:
     #   print("Tienes que pagar más de 20 euros")
#else:
     #   print("Ya has pagado")


# Obtener si el usuario ha pagado
hasPagado = input("¿Has pagado? (true/false): ").strip().lower()

#Convertir la entrada a booleano
if hasPagado == "true":
    hasPagado = True 
elif hasPagado == "false":
    hasPagado = False
else:
    print("Entrada no válida, Introduce 'true' o 'false'.")
    hasPagado = None

# Obtener el precio si la entrada anterior fue válida
if hasPagado is not None:
    precio = float(input("Introduce el precio: "))

    # Condicional IF anidado
    if not hasPagado:
        print("No ha pagado")
        if precio <= 20:
            print("Tienes que pagar menos de 20 euros")
        else:
            print("Tienes que pagar más de 20  euros")
    else:
        print("Ya has pagado")