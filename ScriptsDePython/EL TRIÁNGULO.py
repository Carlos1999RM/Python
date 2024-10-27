
#EL TRIÁNGULO:

#En una obra es necesario construir para el tejado de una casa una estructura triangular con tres
#piezas. El ingeniero se pregunta si dadas la largura de las piezas que ha recibido podrá construir
#este estructura. Crea un script que dados tres longitudes indique si podría construirse un triangulo
#con esas piezas.
#(Pista: la suma de dos piezas tiene que ser mayor que el lado restante. Esto debe ser así para
#todas las posibles combinaciones)

# Solicitar las longitudes de las piezas al usuario
lado1 = int(input("Ingrese la longitud del primer lado: "))
lado2 = int(input("Ingrese la longitud del segundo lado: "))
lado3 = int(input("Ingrese la longitud del tercer lado: "))

# Verificar si se puede construir un triángulo con las piezas
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Se puede construir un triángulo con las piezas")
else:
    print("No sé puede construir un triángulo con las piezas.")

#Explicación del código:
#Solicitud de longitudes al usuario:

#Se solicitan las longitudes de las tres piezas al usuario mediante input. 
#Se usa float para permitir números decimales.
#Verificación de la condición del triángulo:

#Se verifica que la suma de las longitudes de cada par de piezas sea mayor 
#que la longitud de la pieza restante. Esta condición debe cumplirse para las tres combinaciones posibles:
#lado1 + lado2 > lado3
#lado1 + lado3 > lado2
#lado2 + lado3 > lado1
#Imprimir el resultado:

#Si las tres condiciones se cumplen, se imprime que es posible construir un triángulo con las piezas.
#Si alguna de las condiciones no se cumple, se imprime que no es posible construir un triángulo con las piezas.
#Este script permite al usuario ingresar las longitudes de tres piezas y determina de manera clara y 
#directa si es posible construir un triángulo con esas piezas.