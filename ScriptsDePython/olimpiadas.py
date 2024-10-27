#OLIMPIADAS: 

#En la competición de skeleton de las olimpiadas de invierno hay tres finalistas. El cronómetro mide 
#los siguientes tiempos:

#Hannah Neise:   8 minutos 3 segundos y 10 centésimas
#Jackie Narracott:  12 minutos 7 segundos y 8 centésimas
#Kimberley Bos:   9 minutos 14 segundos y 3 centésimas

def convertir_a_segundos(minutos, segundos, centesimas):
    return minutos * 60 + segundos + centesimas / 100

def calcular_velocidad_media(distancia, tiempo_en_segundos):
    return distancia / tiempo_en_segundos

# Distancia de la pista
distancia = 100  # metros

# Solicitar los tiempos para cada finalista
print("Introduce los tiempos para cada finalista en el formato minutos, segundos, centésimas")

# Hannah Neise
minutos_hannah = int(input("Minutos de Hannah Neise: "))
segundos_hannah = int(input("Segundos de Hannah Neise: "))
centesimas_hannah = int(input("Centésimas de Hannah Neise: "))

# Jackie Narracott
minutos_jackie = int(input("Minutos de Jackie Narracott: "))
segundos_jackie = int(input("Segundos de Jackie Narracott: "))
centesimas_jackie = int(input("Centésimas de Jackie Narracott: "))

# Kimberley Bos
minutos_kimberley = int(input("Minutos de Kimberley Bos: "))
segundos_kimberley = int(input("Segundos de Kimberley Bos: "))
centesimas_kimberley = int(input("Centésimas de Kimberley Bos: "))

# Convertir los tiempos a segundos
tiempo_hannah = convertir_a_segundos(minutos_hannah, segundos_hannah, centesimas_hannah)
tiempo_jackie = convertir_a_segundos(minutos_jackie, segundos_jackie, centesimas_jackie)
tiempo_kimberley = convertir_a_segundos(minutos_kimberley, segundos_kimberley, centesimas_kimberley)

# Calcular las velocidades medias
velocidad_hannah = calcular_velocidad_media(distancia, tiempo_hannah)
velocidad_jackie = calcular_velocidad_media(distancia, tiempo_jackie)
velocidad_kimberley = calcular_velocidad_media(distancia, tiempo_kimberley)

# Imprimir los resultados
print(f"Hannah Neise: {velocidad_hannah:.2f} metros/segundo")
print(f"Jackie Narracott: {velocidad_jackie:.2f} metros/segundo")
print(f"Kimberley Bos: {velocidad_kimberley:.2f} metros/segundo")
