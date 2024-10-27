# RED SOCIAL: 

#Una red social tiene una base de datos de usuarios y sus correspondientes amistades. 
#Crea un programa que tome una base de datos de una red social como una lista de 
#tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los 
#nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas 
#diferentes. Deberas eliminar las cuentas duplicadas y después  devolver una tupla de 
#tuplas que contiene el número real de amigos por usuario y el usuario con más amigos. 
#Pista 1: Tus datos de entrada podrían ser así  —>  red_social = [("Juan", ["Maria", "Pedro", 
#"Luis"]), ("Maria", ["Juan", “Pedro”,”Juan”]), ("Pedro", ["Juan", "Maria"]), ("Luis", [“Juan”])] 
#Pista 2: Para eliminar duplicidades puedes usar sets
print("-------------------------------------------------------------------------------------------------------------")

# Datos de entrada
red_social = [
    ("Juan", ["Maria", "Pedro","Luis"]),
    ("Maria",["Juan", "Pedro", "Juan"]),
    ("Pedro",["Juan", "Maria","Maria"]),
    ("Luis", ["Juan", "Maria","Pedro"])
]

# Diccionario para almacenar el número de amigos únicos por usuario
amigos_únicos = {}

# Recorrer cada usuario y su lista de amigos
for usuario, amigos in red_social:
    # Eliminar duplicados convirtiendo la lista de amigos a un conjunto
    amigos_únicos[usuario] = len(set(amigos))

# Convertir el diccionario a una lista de tuplas con el número de amigos únicos
num_amigos = list(amigos_únicos.items())

# Encontrar el usuario con más amigos
usuario_con_más_amigos = max(num_amigos, key=lambda x: x[1])

# Resultado final
resultado = (tuple(num_amigos), usuario_con_más_amigos)

# Imprimir por pantalla
print("Result:",resultado)
print("-------------------------------------------------------------------------------------------------------------")

#<###############################################################################################################################################>#

#LA BIBLIOTECA: 
#Una biblioteca tiene una lista de libros y sus autores. Crea un programa que tome la lista 
#de libros y sus autores como una lista de tuplas, donde cada tupla contiene el título del 
#libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del 
#libro y el apellido del autor. 
#Pista: Tus datos de entrada podrían ser así  —> lista_libros = [(‘El aleph', ‘Jorge Luis 
#Borges'), ('Cien años de soledad', ‘Garbriel Garcia Márquez'), ('La ciudad y los perros', 
#‘Mario Vargas Llosa')] 

# Lista de libros
list_books = [
    ('El aleph', 'Jorge Luis Borges'),
    ('Cien años de soledad', 'Gabriel Garcia Márquez'),
    ('La ciudad y los perros', 'Mario Vargas Llosa')
]

# Nueva lista con el título del libro y el apellido del autor
new_list_books = []

for title, author in list_books:
    # Obtener el apellido del autor
    lastName = author.split()[2]
    # Añadir la nueva tupla a la lista
    new_list_books.append((title, lastName))

# Imprimir la nueva lista de libros
print("Result:",new_list_books)
print("-------------------------------------------------------------------------------------------------------------")

#<###############################################################################################################################################>#

#DATOS CLIENTES: 
#Una compañía tiene dos bases de datos de clientes. La primera base de datos contiene 
#el nombre del cliente, la dirección de correo electrónico y el número de teléfono. La 
#segunda base de datos contiene el nombre del cliente, la dirección y el historial de 
#pedidos. Escribe un programa que tome las dos bases de datos como listas de tuplas y 
#devuelva una nueva lista de tuplas que contenga solo los clientes que aparecen en 
#ambas bases de datos. Los clientes se consideran iguales si tienen el mismo nombre. 
#Pista: Tus datos de entrada podrían ser así  —>   
#base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria", 
#"maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", 555-9012)] 
# = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]), 
#("Luis", "Calle 789", ["Libro4"])]

base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria", 
"maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", 555-9012)] 

base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]), 
("Luis", "Calle 789", ["Libro4"])]

# Nueva lista de clientes que aparecen en ambas bases de datos
clientes_comunes = []

# Recorrer la primera base de datos
for cliente1 in base_datos1:
    nombre1 = cliente1[0] # Obtener el nombre del cliente de la primera base de datos
    
    # Recorrer la segunda base de datos
    for cliente2 in base_datos2:
        nombre2 = cliente2[0] # Obtener el nombre del cliente de la segunda base de datos

      # Comparar los nombres de los clientes
        if nombre1 == nombre2:
            clientes_comunes.append(cliente1)
            
# Imprimir la nueva lista de clientes comunes
print("Result:",clientes_comunes)
print("-------------------------------------------------------------------------------------------------------------")
