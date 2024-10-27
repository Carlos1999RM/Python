#BECAS PARA ESTUDIANTES (BONUS*):
#El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media.
#Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Crea un script que
#pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no.
#*Los ejercicios bonus no se resolverán directamente en clase si no que están pensados para que
#los alumnos los discutan por el chat de Discord y compartan sus soluciones. Las soluciones
#compartidas de los alumnos se subirán en un archivo a la academia.


def puede_optar_a_beca(name, age,average_note):
    if 17 < age <= 21 and average_note >= 8:
        return True
    else:
        return False
    
    # Solicitar datos del estudiante

name = (input("Introduzca su nombre: "))
age = int(input("Ingrese su edad: "))
average_note = float(input("Ingrese la nota media del estudiante: "))

# Verificar si puede optar a la beca
if puede_optar_a_beca(name, age, average_note):
    print(f"{name} puede optar a la beca.")
else:
    print(f"{name} no puede optar a la beca.")