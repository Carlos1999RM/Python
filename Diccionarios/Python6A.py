#EJERCICIOS HOJA 6 
#TEMA: DICCIONARIOS
#OBJETIVO: FAMILIARIZACIÓN CON EL USO DE DICCIONARIOS, 
#SUS CARACTERÍSTICAS Y METODOS ASOCIADOS
#EJERCICIOS 6A  
###---<!############################################################################################################>---###

#TRABAJANDO CON DICCIONARIOS: 
# 1. Crea un diccionario vacío llamado “mi_diccionario”. 

mi_diccionario = {}

# 2. Agrega un par clave-valor a "mi_diccionario" donde la clave sea "nombre" y el valor 
# sea tu nombre. 
mi_diccionario['nombre'] = 'carlos'

# 3. Accede e imprime el valor asociado con la clave "nombre" en “mi_diccionario". 
print(mi_diccionario['nombre'])

# 4. Verifica si la clave "edad" existe en "mi_diccionario". Imprime "True" si existe y "False" 
# en caso contrario.
verificar = 'edad'
if verificar in mi_diccionario:
    print(f"{verificar} is True")
else:
    print(f"{verificar} is false")

# 5. Crea un diccionario llamado "estudiante" con los siguientes pares clave-valor: 
# "nombre" con el nombre del alumno, "edad" con su edad y "materia" con su materia 
# favorita.
estudiante = {'nombre': 'Alexei', 'edad': 27, 'materia': 'Cryptonita'}

# 6. Actualiza el valor de la clave "edad" en el diccionario "estudiante" para reflejar la edad 
# actual de tu amigo.  
estudiante['edad'] = 30
print(estudiante)

# 7. Elimina el par clave-valor con la clave "materia" del diccionario “estudiante".  
del estudiante['materia'] 
print(estudiante)

# 8. Imprime todas las claves en el diccionario “estudiante".  
print(estudiante)

# 9. Crea un diccionario llamado "agenda" con tres entradas: "Juan" con el valor 
# "1234567890", "Joana" con el valor "9876543210" y "Jimena" con el valor 
# “5555555555”. 
agenda = {'Juan': 1234567890, 'Joana': 9876543210, 'Jimena': 5555555555} 

# 10. Agrega una nueva entrada al diccionario "agenda" con la clave "Julio" y el valor “9998887777".
agenda['Julio'] = 9998887777
print(agenda)

# 11. Imprime el número de entradas (pares clave-valor) en el diccionario “agenda".
número_de_entradas = len(agenda)
print(f"El diccionario tiene {número_de_entradas} entradas.")

# 12. Crea una lista llamada "claves" que contenga todas las claves del diccionario “agenda". 
claves = ['Juan','Joana','Jimena']

# 13. Verifica si la clave "Juan" existe en el diccionario "agenda". Imprime "True" si existe y "False" en caso contrario.
verificar_nombre = 'Juan'

if verificar_nombre in agenda:
    valor_de_la_clave = agenda[verificar_nombre]
    if valor_de_la_clave:
        print(f"{verificar_nombre} is true")
    else:
        print(f"{verificar_nombre} is false")
else:
    print(f"{verificar_nombre} no está en el dicionario")

# 14. Elimina la entrada con la clave “Jimena”. 
del agenda['Jimena']
print(agenda)

# 15. Utiliza un bucle for para iterar sobre todas las claves en el diccionario "agenda" e 
# imprime cada par clave-valor en el formato "Nombre: Número”.  
for clave in agenda:
    valor = agenda[clave]
    print(f"Clave: {clave}, valor: {valor}")

# 16. Utiliza el método "get()" para obtener el valor asociado con la clave "Juan" en el 
# diccionario "agenda". Si la clave no existe, imprime "Clave no encontrada”.
verificar_con_get = agenda.get('Juan')

if verificar_con_get is not None:
    print(f"Valor asociado para Juan: {verificar_con_get}")
else:
    print(f"Clave no encontrada.")

# 17. Borra todas las entradas del diccionario “agenda”.
claves_eliminar = ['Juan','Jimena','Joana', 'Julio']

for clave in claves_eliminar:
    if clave in agenda:
        del agenda[clave]

print(agenda)


###---<!############################################################################################################>---###
########LISTAS DE DICCIONARIOS: #########
# 18. Crea una lista llamada "estudiantes" que contenga dos diccionarios. Cada diccionario 
# representa a un estudiante y tiene las claves "nombre" y "edad" con sus respectivos 
# valores. Recorre la lista e imprime el nombre y edad de cada estudiante.
# Lista inicial de estudiantes
estudiantes = [
    {"nombre": "Alice", "edad": 30},
    {"nombre": "Bob", "edad": 25}
]

# 1. Imprimir la lista original
print("Lista original:")
for estudiante in estudiantes:
    print(estudiante)

# 2. Agregar un nuevo estudiante
nuevo_estudiante = {"nombre": "Charlie", "edad": 28}
estudiantes.append(nuevo_estudiante)

# Imprimir la lista actualizada después de agregar el nuevo estudiante
print("\nLista después de agregar un nuevo estudiante:")
for estudiante in estudiantes:
    print(estudiante)

# 3. Eliminar el estudiante con nombre 'Alice' y edad 30
nombre_a_eliminar = 'Alice'
edad_a_eliminar = 30

estudiantes = [estudiante for estudiante in estudiantes if not (estudiante["nombre"] == nombre_a_eliminar and estudiante["edad"] == edad_a_eliminar)]

# Imprimir la lista actualizada después de eliminar el estudiante
print("\nLista después de eliminar el estudiante:")
for estudiante in estudiantes:
    print(estudiante)

# 4. Actualizar la edad del estudiante con nombre 'Bob'
nombre_a_actualizar = "Bob"
nueva_edad = 27

for estudiante in estudiantes:
    if estudiante["nombre"] == nombre_a_actualizar:
        estudiante["edad"] = nueva_edad
        break  # Salir del bucle después de la actualización

# Imprimir la lista final después de actualizar la edad
print("\nLista después de actualizar la edad del estudiante:")
for estudiante in estudiantes:
    print(estudiante)

###---<!############################################################################################################>---###
####ANIDAMIENTO DE DICCIONARIOS:####
# 22.  Crea un diccionario llamado "productos" que contenga dos entradas. Cada entrada 
# representa un producto y tiene a su vez las claves "nombre" y "precio" con sus 
# respectivos valores. Recorre el diccionario e imprime el nombre y precio de cada 
# producto.

productos = [{'nombre': 'TV-HD4K', 'precio': 1680}, {'nombre': 'Macbook', 'precio': 1200}]

for producto in productos:
    print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}")

# 23.  Agrega un nuevo producto al diccionario "productos" utilizando una nueva clave y 
# valor. Imprime el diccionario actualizado.
nuevo_producto = {'nombre': 'SmartPhone', 'precio': 565}
productos.append(nuevo_producto)

for producto in productos:
    print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}")

# 24. Crea un diccionario llamado "equipos" que contenga tres entradas. Cada entrada 
# representa un equipo deportivo y tiene las claves "nombre" y "jugadores" con sus 
# respectivos valores. Los valores de "jugadores" deben ser listas con los nombres de 
# los jugadores. Recorre el diccionario e imprime el nombre del equipo y la lista de 
# jugadores.

equipos = [
    {'nombre': 'juventus', 'jugadores': ['roberto', 'josé', 'camuñas', 'alvaro']},
    {'nombre': 'sevilla', 'jugadores': ['carlos', 'pau', 'camuñas', 'guille']},
    {'nombre': 'pamplona', 'jugadores': ['pedro', 'josé', 'rafa', 'alvaro']}
]

# Recorrer el diccionario e imprimir el nombre del equipo y la lista de jugadores
for equipo in equipos:
    print(f"Nombre del equipo: {equipo['nombre']}, Jugadores: {equipo['jugadores']}")


# 25. Agrega un nuevo equipo al diccionario "equipos" utilizando una nueva clave y valor. 
# La lista de jugadores debe contener al menos tres nombres. Imprime el diccionario 
# actualizado.
# Agregar un nuevo equipo al diccionario
nuevo_equipo = {'nombre': 'jerez', 'jugadores': ['juan', 'josé', 'alexi', 'nicolás']}
equipos.append(nuevo_equipo)

# Imprimir el diccionario actualizado
for equipo in equipos:
    print(f"Nombre: {equipo['nombre']}, Jugadores: {equipo['jugadores']}")

# 26. Actualiza la lista de jugadores de uno de los equipos existentes en el diccionario 
# "equipos". Agrega un nuevo jugador a la lista. Imprime el diccionario actualizado. 
# Agregar un nuevo jugador al equipo 'sevilla'
# Agregar un nuevo jugador al equipo 'sevilla'
nuevo_jugador = 'kiki'
for equipo in equipos:
    if equipo['nombre'] == 'sevilla':
        equipo['jugadores'].append(nuevo_jugador)
        break

# Imprimir el diccionario actualizado
for equipo in equipos:
    print(f"Nombre: {equipo['nombre']}, Jugadores: {equipo['jugadores']}")
