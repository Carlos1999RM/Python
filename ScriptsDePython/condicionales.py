#Condicionales: if
#La declaración if se usa para ejecutar código condicionalmente, según si una condición es verdadera o falsa.

#Ejemplo de if


#print("Introduce número")
#x = int(input())
#if (x > 10) :
   # print("Es mayor")
#elif (x == 10):
  #  print("Es igual")
#else:
   # print("Es menor")

#Estructura switch-case
#Python no tiene una declaración switch-case como otros lenguajes de programación (como C o Java),
#pero se puede emular usando diccionarios o con funciones.

#"Ejemplo usando diccionario"
# Ejemplo de switch-case usando diccionario
#def switch_case_day(day):
        # Creamos un diccionario donde las claves son números y los valores son los nombres de los días
  #      switcher = {
        #     1: "Monday",
       #      2: "Tuesday",
       #      3: "Wednesday",
       #      4: "Thursday",
        #     5: "Friday",
       #      6: "Saturday",
       #      7: "Sunday"
    #    }
        # Retornamos el valor correspondiente a la clave 'dia' o "Día inválido" si 'dia' no está en el diccionario
     #   return switcher.get(day, "Invalid day")

# Usando la función
#day = int(input())
#print(switch_case_day(day))  # Imprimimos el resultado de llamar a switch_case_dia con el valor de dia8

"Ejemplo usando funciones"

# Ejemplo de switch-case usando funciones
# Definimos funciones para cada día de la semana

def monday():
    return("Today is monday")
def tuesday():
    return("Today is Tuesday")
def wednesday():
    return("Today is Wednesday")
def Thursday():
    return("Today is Thursday")
def Friday():
    return("Today is Friday")
def Saturday():
     return("Today is Saturday")
def Sunday():
    return("Today is Sunday")
def invalid_day():
    return("Invalid day")

# Función que emula el comportamiento de switch-case
def switch_case_day(day):
         # Creamos un diccionario donde las claves son números y los valores son funciones
        switcher = {
           1: monday,
           2: tuesday,
           3: wednesday,
           4: Thursday,
           5: Friday,
           6: Saturday,
           7: Sunday
        }
        # Obtener la función correspondiente y ejecutarla
        # Si 'dia' no está en el diccionario, ejecuta la función dia_invalido
        return switcher.get(day, invalid_day)()
day = int(input("Introduce un número de día (1 - 7): "))
print(switch_case_day(day))