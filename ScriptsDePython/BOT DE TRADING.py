
#BOT DE TRADING:
#Un bot de trading está programado para realizar ciertas acciones con respecto a un producto
#financiero. Crea un script de manera que dado un precio introducido por el usuario, si el precio del
#producto está por debajo de 100 dólares, el bot imprima por pantalla la orden de comprar. Si está
#entre 100 y 150 dolores (ambos incluidos) el bot deberá imprimir la orden de hold. Si el precio está
#estrictamente por encima de 150 el bot deberá imprimir la orden de vender.

## Pedimos un precio al usuario
precio = int(input("Ingresa el precio en dólares: "))

## Comprobar el precio y ver si debemos comprar, holdear o vender
if precio < 100:
    print("Es hora de comprar")
elif 100 <= precio <= 150:
    print("Toca holdear")
else:
    print("Es hora de verder")
