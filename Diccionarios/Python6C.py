'''GESTIÓN DE EMPLEADOS: 
Imagina que eres el gerente de recursos humanos de una empresa y 
necesitas gestionar la información de los empleados. Cada empleado 
tiene un nombre, salario y departamento al que pertenece. Implementa 
un programa en Python que permita agregar nuevos empleados, 
actualizar el salario de un empleado existente, mostrar la lista completa 
de empleados y calcular el promedio salarial por departamento.
'''
'''''
empleados = {}

continuar = True
while continuar:
    print("1. Agregar empleado")
    print("2. Actualizar salario de empleados")
    print("3. Mostrar lista de empleados")
    print("4. Calcular promedio salarial por departamento")
    print("5. Salir")
    opción = input("Seleccione una opción.")

    # Agregar empleado
    if opción == '1':
        nombre = input("Ingrese nombre del empleado: ")
        salario = float(input("Ingrese salario del empleado: "))
        departamento = input("Ingrese departamento del empleado: ")

        empleados[nombre] = {
            "salario": salario,
            "departamento": departamento,
        }

        print("Empleado agregado exitosamente")

    # Actualizar salario empleados
    elif opción == "2":
        nombre = input("Ingrese el nombre del empleado: ")
        # comprobamos la existencia del empleado en la base de datos
        if nombre in empleados:
            # pedimos nuevo salario
            nuevo_salario = float(input("Ingrese el nuevo salario del empleado: "))
            # actualizamos salario del empleado
            empleados[nombre]["salario"] = nuevo_salario
            print("Salario actualizado exitosamente")
        else:
            print("Empleado no encontrado.")

    # Mostrar lista de empleados
    elif opción == "3":
        print("Lista de empleados: ")
        # Recorremos pares clave-valor = nombre-datos
        for nombre, datos_empleado in empleados.items():
            salario = datos_empleado["salario"] # extraemos valor del salario
            departamento = datos_empleado["departamento"] # extraemos departamento
            # imprimimos información
            print(f"Nombre: {nombre}, Salario: {salario}, Departamento: {departamento}")
        
    # Calcular promedio salarial por departamento
    elif opción == '4':
        departamento = input("Ingrese el departamento: ")
        # inicializamos variables
        total_salarios = 0
        contador = 0
        # recorremos datos de los empleados en los valores del dict
        for datos_empleado in empleados.values():
            # si el departamento coincide sumaos el salario
            if datos_empleado["departamento"] == departamento:
                total_salarios = total_salarios + datos_empleado["salario"]
                contador = contador + 1
        
        # si hay empleados en el departamento calculamos el promedio
        if contador > 0:
            promedio_salario = total_salarios / contador
            print(f"Promedio salarial del departamento {departamento}: {promedio_salario}")
        # si no hay empleados en el departamento lo indicamos
        else:
            print(f"No hay empleados en el departamento { departamento}")

    elif opción == '5':
        print("Cerrando programa.")
        continuar = False

    else:
        print("Opción inválida. Por favor, seleccionamos una opcón válida.")

'''
'''ANÁLISIS DE VOTACIONES: 
Supongamos que tienes los resultados de una elección con los nombres 
de los candidatos y la cantidad de votos obtenidos por cada uno. 
Implementa un programa en Python que permita registrar los votos, 
mostrar la lista completa de candidatos y sus votos, encontrar al 
candidato ganador (con más votos) y calcular el porcentaje de votos que 
obtuvo cada candidato. 
'''

resultados = {}
continuar = True
while continuar:
    print("1. Registrar voto")
    print("2. Mostrar lista de candidatos.")
    print("3. Encontrar candidatos ganador.")
    print("4. Calcular porcentaje de votos.")
    print("5 Salir.")

    opción2 = input("Seleccione una opción: ")

    # Registar voto
    if opción2 == '1':
        # pedimos nombre de candidatos
        candidato = input("Ingrese nombre del candidato: ")
        # comprobamos si el candidato está en la base de datos
        if candidato in resultados:
            # sumamos voto
            resultados[candidato] = resultados[candidato] + 1
            # si no está en la base de datos añadidos par clave valor
        else:
            # añadimos voto
            resultados[candidato] = 1
        
        # Mostrar lista de candidatos y votos
    elif opción2 == '2':
        print("Lista de candidatos y votos: ")
        for candidato, votos in resultados.items():
            # imprimimos candidatos-votos
            print(f"Candidatos: {candidato}, Voto: {votos}")
        
        # Encontrar candidatos ganador
    elif opción2 == '3':
        # comprobamos si se ha votado ya
        # si no
        if len(resultados) == 0:
            print("No hay candidatos registrados.")
            # si no hay votaciones registradas
        else:
            # extraemos la clave asociada al número de votos más alto
            ganador = max(resultados, key= resultados.get)
            print(f"El candidato ganador es: {ganador}.")

        # Calcular el procentaje de votos
    elif opción2 == '4':
        total_votos = sum(resultados.items())
        print("Porcentaje de votos por candidato")
        for candidato, votos in resultados.items():
            porcentaje = (votos/total_votos) * 100
            print(f"Candidato: {candidato}, Porcentaje de votos {porcentaje:.2f}%")

        # Cerrar script
    elif opción2 == '5':
        print("Cerrando votaciones.")
        continuar = False

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")