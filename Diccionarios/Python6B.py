'''''
REGISTRO DE VENTAS: 
Tienes una tienda y deseas realizar un seguimiento de las ventas diarias 
de tus productos. Cada producto tiene un nombre y una cantidad 
vendida. Implementa un programa en Python que utilice un diccionario 
para almacenar la información de las ventas. El programa debe permitir 
registrar las ventas de productos, actualizar la cantidad vendida de un 
producto existente y calcular el total de ventas diarias. 
(Pista: puedes comenzar con un diccionario vacío e ir añadiendo cada 
producto)
'''''

# Inicializar el diccionario para almacenar las ventas
ventas_diarias = {}

def registrar_venta(producto, cantidad):
    if producto in ventas_diarias:
        ventas_diarias[producto] += cantidad
    else:
        ventas_diarias[producto] = cantidad

def total_ventas():
    return sum(ventas_diarias.values())

# Ejemplo de uso
registrar_venta("Manzana", int(input("Cantidad de Manzanas vendidas: ")))
registrar_venta("Plátano", int(input("Cantidad de Plátanos vendidos: ")))
registrar_venta("Fresas", int(input("Cantidad de Fresas vendidas: ")))


print("Ventas diarias:", ventas_diarias)
print("Total de ventas:", total_ventas())

'''###############################################################################################################'''

print("--------------------------------------------------------------------------------")

'''''
ADMINISTRACION DE PROYECTOS: 
Eres un gerente de proyectos y necesitas un programa para administrar 
las tareas y responsabilidades de tu equipo. Cada tarea tiene un nombre, 
una descripción y un responsable asignado. Implementa un programa en 
Python que utilice un diccionario para almacenar la información de las 
tareas. El programa debe permitir agregar nuevas tareas, asignar 
responsables a las tareas existentes, actualizar las descripciones de las 
tareas y mostrar la lista completa de tareas y responsables.  
(Pista: puedes comenzar con un diccionario vacío y construir un 
diccionario de diccionarios)
'''''

# Diccionario base de datos
tareas = {}

# Agregar tareas nuevas
tareas["tarea 1"] = {"descripcion": "Realizar análisis de requisitos", "responsable": "Carlos"}
tareas["tarea 2"] = {"descripcion": "Desarrolladora", "responsable": "Marta"}
tareas["tarea 3"] = {"descripcion": "Validación de procesos", "responsable": "Sara"}

# Asignar responsable a las tareas existentes
tareas["tarea 1"]["responsable"] = "Alexei"
tareas["tarea 3"]["responsable"] = "María"

# Actualizar las descripciones de las tareas
tareas["tarea 2"]["descripcion"] = "Realizar test de hiperparámetros"

# Mostrar la lista de tareas y responsables
#print("Lista de tareas y responsables")
#for tarea, detalles in tareas.items():
    #print("Tarea", tarea)
    #print("Descripción: ", detalles["descripcion"])
    #print("Responsable: ", detalles["responsable"])
    #print()

print("--------------------------------------------------------------------------------")

'''REGISTRO DE ASISTENCIAS: 
Eres un profesor y deseas realizar un seguimiento de la asistencia de tus 
estudiantes a lo largo del semestre. Cada estudiante tiene un nombre y 
una lista de fechas en las que asistió a clases. Implementa un programa 
en Python que utilice un diccionario para almacenar la información de las 
asistencias. El programa debe permitir registrar la asistencia de los 
estudiantes, agregar nuevas fechas de asistencia y mostrar la lista de 
estudiantes y las fechas en las que asistieron. 
(Pista: puedes comenzar con un diccionario vacío y construir un 
diccionario de listas) 
'''

# Diccionario base de datos
asistencias = {}
#asistencias = dict()

# Registrar asistencias de estudiantes
asistencias["Estudiante_1"] = ["2022-02-01", "2022-02-04", "2022-02-07"]
asistencias["Estudiante_2"] = ["2022-02-02", "2022-02-05", "2022-02-04"]
asistencias["Estudiante_3"] = ["2022-02-01", "2022-02-09", "2022-02-12"]

# Agregar nuevas fechas de asistencia para un estudiante existente
asistencias["Estudiante_1"].append("2022-02-01")
asistencias["Estudiante_2"].append("2022-02-05")

# Mostrar la lista de estudiantes y las fechas en las que asistieron
#print("Registro de asistencias: ")
#for estudiante, fechas in asistencias.items():
    #print("Estudiante: ", estudiante)
    #print("Fechas de asistencia: ", ", ".join(fechas))

print("--------------------------------------------------------------------------------")
'''REGISTRO DE PUNTAJES: 
Implementa un programa en Python que permita registrar y mantener un 
seguimiento de los puntajes de un juego. El programa debe permitir a los 
jugadores ingresar sus nombres y puntajes, almacenarlos en un 
diccionario y proporcionar funcionalidades para mostrar el puntaje más 
alto, el promedio de puntajes y la cantidad total de jugadores. 
'''

# base de datos con puntajes
registros = {}
continuar = True
# seguimiento de los puntajes --> actualizados
while continuar:
    # Pedir al usuario su nombre
    #name = input("Ingrese nombre del jugador (o 'salir' para terminar): ")
    #if name.lower() == 'salir':
        continuar = False
    #else:
        #score = int(input("Ingrese el puntaje del jugador: "))
        #registros[name] = score

    # Obtener puntaje más alto
    #jugador_mas_alto = max(registros, key=registros.get)
    #puntaje_mas_alto = registros[jugador_mas_alto]
    #print("Puntaje más alto: ")
    #print("Jugador: ", jugador_mas_alto)
    #print("Puntaje: ", puntaje_mas_alto)

    # Obtener el promedio de puntajes
    #total_puntajes = sum(registros.values())
    #cantidad_jugadores = len(registros)
    #promedio = total_puntajes / cantidad_jugadores
    #print("Promedio de puntajes: ", promedio)

    # Cantidad total de jugadores
    #print("La cantidad de jagadores es: ", cantidad_jugadores)