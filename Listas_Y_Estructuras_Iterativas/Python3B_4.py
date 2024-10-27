#EL COMERCIAL:

#Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un
#programa para realizar un seguimiento de los productos que has vendido y el valor total de las
#ventas. Supongamos que hay un total de 10 productos.
#Tú has vendido 5 de estos productos en las siguientes cantidades:
#Producto 1: 3 unidades
#Producto 2: 1 unidad
#Producto 5: 7 unidades
#Producto 6: 2 unidades
#Producto 9 : 4 unidades
#Los precios de cada uno de estos productos son como siguen:
#Producto 1: 30.0 EU	 	 Producto 6: 44.0 EU
#Producto 2: 9.8 EU	 	 Producto 7: 21.2 EU
#Producto 3: 42.5 EU	 	 Producto 8: 53.2 EU
#Producto 4: 32.6 EU	 	 Producto 9: 25.3 EU
#Producto 5: 71.5 EU	 	 Producto 10: 57.8 EU
#Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima
#la cantidad total de ventas, el dinero facturado por producto y el dinero total.

# Definimos los productos y sus precios
precio_productos = {
    1: 30.0,
    2: 9.8,
    3: 42.5,
    4: 32.6,
    5: 71.5,
    6: 44.0,
    7: 21.2,
    8: 53.2,
    9: 25.3,
    10: 57.8
}

# Definimos las unidades vendidas de los productos
unidades_vendidas = {
    1: 3,
    2: 1,
    5: 7,
    6: 2,
    9: 4
}

# Inicializamos las variables para calcular el dinero total facturado
dinero_total = 0
ventas_por_productos = {}

# Calculamos el dinero facturado por cada producto y el total
for producto, unidades in unidades_vendidas.items():
    precio = precio_productos[producto]
    dinero_producto = unidades * precio
    ventas_por_productos[producto] = dinero_producto
    dinero_total += dinero_producto


# Imprimimos el resultado
print("Cantidad total de ventas productos: ")
for producto, dinero in ventas_por_productos.items():
    print(f"Producto {producto}: {dinero: .2f} EU")

print(f"\nDinero total facturado: {dinero_total:.2f} EU")