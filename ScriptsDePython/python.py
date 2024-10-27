#print("¿Cómo te llamas?")
#name = input()
#print("Nice to meet you", name,". ")

#number = float(input("¿Cúantos años tienes? "))
#print("Entonces has vivido aproximadamente", 365 * number, "dias")

#<!------------------------------------------------------------------->

#name = 'Carlos Richarte'
#print(name.title())

#string = 'Hola.Mundo'
#print(string.replace("."," "))


#name = "Santiago"
#lastName = 'y cierra España'
#complete_name = name + " " + lastName
#print(complete_name)

#print("Lenguajes: \nJavaScript\nPython\nJava\nSQL\nHTML\nCSS\nPHP")

#<!------------------------------------------------------------------->

#EJERCICIOS HOJA 1
#TEMA: VARIABLES, TIPOS DE DATOS Y OPERACIONES BÁSICAS
#OBJETIVO: FAMILIARIZACIÓN CON LA SINTAXIS BÁSICA DE PYTHON, CON LAS 
#FUNCIONES DE LECTURA Y ESCRITURA Y CON EL USO DE OPERACIONES BÁSICAS
#MENSAJE DE BIENVENIDA:

#El objetivo de este ejercicio es que crees un script que dado un nombre de usuario le de la 
#bienvenida con su nombre en el formato correcto

# Cadena original
#str = 'ESTÁS USANDO PYTHON.'
#print(str.lower()) # Convertir y mostrar en minúsculas

# Solicitar el nombre del usuario
#print("¿Cómo te llamas?")
#name = input()

# Capitalizar el nombre del usuario
#name = name.capitalize()

# Construir y convertir la cadena completa a minúsculas excepto el nombre capitalizado
#menssage = f"HOLA {name}, ESTÁS USANDO PYTHON!".lower()

# Reemplazar el nombre en el mensaje para que conserve la capitalización
#menssage = menssage.replace(name.lower(), name)

# Imprimir el mensaje final
#print(menssage)

#<!------------------------------------------------------------------->

# Cadena original
string = 'Estás usando Python'
print(string.lower()) # Convertir y mostrar en minúsculas

# Solicitar el nombre del usuario
print("¿Cómo te llamas?")
name = input()

# Filtrar solo caracteres alfabéticos y capitalizar el nombre
name = ''.join([char for char in name if char.isalpha()]).capitalize()

# Construir y convertir la cadena completa a minúsculas excepto el nombre capitalizado
message = f"Hola {name}, estás usando Python!".lower()

# Reemplazar el nombre en el mensaje para que conserve la capitalización
message = message.replace(name.lower(), name)

# Imprimir el mensaje final
print(message)


#<!------------------------------------------------------------------->
#Nombre = "Carlos"
#print("Hola " + Nombre + ", estás usando Python!")