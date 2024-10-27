def contraseña_segura(contraseña):
    # Definimos los conjuntos de vocales y símbolos especiales permitidos
    vocales = {"a","e","i","o","u"}
    simbolos_especiales = {"#", "&", "*"}

    # Inicializamos contadores para verificar las condiciones requeridas
    contador_vocales = 0
    simbolos_utilizados = set()

    # Recorremos cada carácter de la contraseña
    for carácter in contraseña:
        if carácter in vocales:
            contador_vocales +=1
        elif carácter in simbolos_especiales:
            simbolos_especiales.add(carácter)

    # Verificamos las condiciones para determinar si es una contraseña segura
    if contador_vocales >= 1 and len(simbolos_utilizados) == 2:
        print("¡La contraseña es segura!")
    else:
        print("La contraseña no cumple con los requisitos de seguridad.")

# Pedimos al usuario que ingrese la contraseña
contraseña_ingresada = input("Ingrese la contraseña a verificar: ")

# Llamamos a la función para verificar la contraseña
contraseña_segura(contraseña_ingresada)