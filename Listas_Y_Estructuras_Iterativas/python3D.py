
#TEMA: USO DE LISTAS Y BUCLES
#OBJETIVO: FAMILIARIZACIÓN CON EL USO DE LISTAS SIMPLES, LISTAS ANIDADAS, SUS
#FUNCIONES ASOCIADAS Y LAS SENTENCIAS CONDICIONALES Y LOS BUCLES EN EL
#CONTEXTO DE LAS LISTAS
#EJERCICIOS 3D

#ANALISIS DE VENTAS:
#Supongamos que eres el propietario de una tienda en línea y tienes una lista de ventas de los
#últimos 30 días. Quieres analizar las ventas por día de la semana para identificar los días de mayor
#venta.
#Pista 1: Puedes crear dos listas, una con las ventas por cada día del mes como por ejemplo…
#ventas = [120, 80, 140, 200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110,
#140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
#Y otra lista con los días de la semana:
#dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", „Domingo“]
#Después puedes crear una nueva lista con una entrada por cada día de la semana y usar un bucle
#para añadir a esta lista la suma de las ventas correspondientes a cada uno de los días de la
#semana.
#Pista 2: Puede que necesites una variable que lleve la cuenta del día de la semana actual y se
#reinicie a cero cuando llegue al séptimo día.

# Listas
ventas = [200, 75, 100, 180, 220, 160, 110, 90, 120, 170, 190, 250, 300, 95, 110,140, 180, 200, 160, 120, 80, 170, 150, 210, 190, 230, 250]
dias_de_la_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Crear una lista para la suma de ventas por día de la semana
suma_ventas_dias = {dia: 0 for dia in dias_de_la_semana}

# Recorrer la lista de ventas y sumar las ventas al día correspondiente
for i, venta in enumerate(ventas):
    dia_actual = dias_de_la_semana[i % len(dias_de_la_semana)]
    suma_ventas_dias[dia_actual] += venta

for dia, suma in suma_ventas_dias.items():  
    print(f"{dia}: {suma}")