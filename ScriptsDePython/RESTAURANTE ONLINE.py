
#RESTAURANTE ONLINE:

#En una hamburguesería han abierto la posibilidad de hacer pedidos online. Ofrecen básicamente
#dos productos de fama mundial: su hamburguesa clásica y la hamburguesa vegana.
#Los ingredientes extra de la hamburguesa clásica son:
#- Queso Idiazabal
#- Bacon
#- Huevo
#Los ingredientes extra de la hamburguesa vegana son:
#- Tofu
#- Cebolla caramelizada
#Crea un script que le pregunte al usuario que tipo de hamburguesa quiere. En función de la
#respuesta debe enseñarle los ingredientes extra disponibles y permitirle escoger uno de ellos.
#Finalmente debe imprimir por pantalla que tipo de hamburguesa se ha elegido y cuales son sus
#ingredientes. 

# Pedir al usuario el tipo de hamburguesa
hamburguesa = input("Que tipo de hamburguesa quieres? (clásica o vegana mi rey?)")

# Comprobamos que hamburguesa ha pedido el usuario
# Si has elegido la clásica
if hamburguesa.lower() == "clasica":
    # Ofrecemos la opción de elegir un ingrediente extra: queso, bacon, huevo
    ingrediente_extra = input("Los ingredientes extra disponibles son: queso idiazabal, cebollita, huevo. Elige uno")

    # Imprimimos que tipo de hamburguesa ha elegido
    if ingrediente_extra.lower() == "queso idiazabal":
        print("Has elegido una hamburguesa con queso idiazabal")
    elif ingrediente_extra.ljust() == "bacon":
        print("Has elegido una hamburguesa clásica con bacon")
    elif ingrediente_extra.lower() == "huevo":
        print("Has elegido clásica con huevo")
    else:
        print("El ingrediente aleccionado no está disponible")

#Si ha elegido la vegana
elif hamburguesa.lower() == "vegana":
 
# Ofrecemos la opciónde elegir un ingrediente extra: tofu, cebolla caramelizada
    ingrediente_extra = input("Los ingredientes extra disponibles son: tofu, cebolla caramelizada. Elige un ingrediente extra.")

# Imprimiremos que tipo de hamburguesa ha elegido
    if ingrediente_extra.lower() == "tofu":
        print("Has elegido una hamburguesa vegana con tofu")
    elif ingrediente_extra.lower() == "cebolla caramelizada":
         print("Has elegido una hamburguesa vegana con cebolla caramelizada")
    else:
        print("E lingrediente seleccionado no estña disponible")
# Si no elige ninguna de las dos
else:
    # Imprimiremos un mensaje de error
    print("Ese tipo de hamburguesa no está disponible.")
