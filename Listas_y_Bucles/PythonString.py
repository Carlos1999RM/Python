#STRING A LISTA:

#Desarrolla un script en Python que dado una cadena de caracteres con la siguiente información:
#nombre, apellido, DNI, código_asignatura, convocatoria, nota1, nota2, nota3 … Por ejemplo:
#David Fernandez 12311267A 43527 2 2.1 4.6 3.4. El script debe crear una lista con esos datos,
#introducirlo en una lista de listas donde se encuentra la información de todos los alumnos e
#imprimir la nota media de los alumnos junto con el DNI.
#Supón ahora que tu input es un string como este:
#‘’'David Fernandez 12311267A 43527 2 9.1 7.6 2.4\n
#Maria Garcia 12316487A 43527 2 7.1 8.6 5.4\n
#Juan Perez 647829236A 43527 2 8.1 8.5 8.4\n ‚’’
#Reescribe el script para que procese ese input adecuadamente e imprima la nota media y el DNI
#de todos los alumnos en ese string. 

# Input de ejemplo
input_string = 'David Fernandez 12311267A 8.1 8.6 7.4, Maria Garcia 12316487A 7.1 8.6 7.4, Juan Perez 647829236A  8.1 8.5 8.4'


def procesar_datos(input_string):
    # Dividir la entrada por líneas
    lines = input_string.strip().split(',')

    # Lista para almacenar la información de todos los alumnos
    students = []

    # Procesar cada línea
    for line in lines:
        dates = line.split()
        name = dates[0]
        lastName = dates[1]
        DNI = dates[2]
        asignature_code = dates[3]
        convocatory = dates[4]
        notes = list(map(float, dates[5:]))

        # Crear la lista del alumno

        student = [name, lastName, DNI, asignature_code, convocatory] + notes
        students = students + [student]

        # Calcular e imprimir la nota media y el DNI de cada alumno
    for student in students:
        DNI = student[2]
        notes = student[5:]
        average_note = sum(notes) / len(notes)
        print(f"DNI: {DNI}, Nota media: {average_note:.2f}")

procesar_datos(input_string)