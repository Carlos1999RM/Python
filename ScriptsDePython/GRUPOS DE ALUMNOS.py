
#GRUPOS DE ALUMNOS:

#En uno de los cursos se ha dividido a una clase en dos grupos A y B. Para mezclar a los alumnos
#lo mejor posible se ha asignado a todas las chicas con nombres empezando por la letra E hasta la
#M en el grupo A y el resto en el B. A los chicos con nombres empezando por la letra A hasta la H y
#R hasta la Z se les ha asignado al grupo A también, el resto están en el B.
#Crea un script que pregunte al usuario si es chica o chico y el nombre. El script debe mostrar por
#pantalla el grupo que le corresponde a ese alumno.
# Pedir por pantalla los datos
genero = input("Ingresa tu género(chica/chico): ")

nombre = input("Ingresa tu nombre: ")
nombres_chicas_A = "EHIJKLM"
nombres_chicos_A = "ABCDEFGHRPSÑLJTUVWXYZ"

# Elegir grupo que corresponde
# chica
if genero.lower() == "chica":
    if nombre[0].upper() in nombres_chicas_A:
        print("Tu grupo es el A")
    else:
        print("Tu grupo es el B")
# Chico
elif genero.lower() == "chico":
    if nombre[0].upper() in nombres_chicos_A:
        print("Tu grupo es el A")
    else: 
        print("tu grupo es el B")
else:
    print("Error: Vuelva a inicializar un sexo válido")