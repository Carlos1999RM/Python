#-- Pedir nombre al usuario --#
nombre = input("Ingresa tu nombre: ")

#-- Saludar al usuario --#
print("¡Hola,", nombre +"!")

#Guardamos ingresos y horas trabajadas
ingresos_hora = 25 # en euros
horas_trabajadas = 40

#Calculamos la ganancia semanal
salario_semanal = ingresos_hora * horas_trabajadas

#Calculamos la ganancia anual
ganancia_anual = salario_semanal * 52

#Imprime ganancia anual por pantalla
print(nombre.title(), "tienes unas ganancias anuales de", ganancia_anual, "euros")

#Pedimos los gastos semanales al usuario
gastos_semanales = float(input("Ingresa tus gastos semanales: "))

#Reduzo los gastos a 3/4 de lo anterior
gastos_semanales = gastos_semanales * 3/4

#Calculamos el gasto anual
gasto_anual = gastos_semanales * 52

# Calculamos los ahorros
ahorro_anual = ganancia_anual - gasto_anual

print("Tu ahorro anual será de", ahorro_anual, "euros")