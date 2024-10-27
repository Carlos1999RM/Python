
#BASE DE DATOS DE UN COLEGIO:

#Trabajas en colegio y estas encargado de mantener un seguimiento de las notas de los
#estudiantes de un clase. En tu base de datos tienes una lista con los nombres de los estudiantes y
#para cada estudiante debes guardar sus notas provenientes de deberes, exámenes y proyectos.
#También necesitas calcular a nota media de cada estudiante y la nota media de la clase al
#completo.
#Pista: Para resolver este problema puedes usar una lista anidada donde guardes las notas para
#cada estudiante. Entonces puedes usar un bucle para recorrer la lista de listas y calcular la nota
#media de cada estudiante. También puedes usar otro bucle para calcular la nota media de toda la
#clase.

# Paso 1: Crear la estructura de datos
# Lista de estudiantes, cada estudiante es una lista con su nombre y sus notas [nombre, [notas]]
students = [
    ['carlos', [6.9,5.8,9]],
    ['romavov',[8,4.7,9.9]],
    ['stephan',[5.4,6.9,8.8]],
    ['alonso',[3.8,9.4,7.8]],
    ['venelli',[5.9,6.9,7.9]],
    ['laura', [11.5,13.2,12.8]],
    ['nuria',[2.8,14,8.7]],
    ['elena',[5.5,6.6,7.7]],
]

# Paso 3: Calcular la media de la clase completa
total_notes = 0
total_count = 0

for name, notes in students:
    average = sum(notes) / len(notes)
    print(f"La nota media de {name} es {average:.2f}")
    total_notes += sum(notes)
    total_count += len(notes)

average_class = total_notes / total_count
print(f"La nota media de la clase es {average_class:.5f}")