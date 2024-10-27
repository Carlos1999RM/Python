''' Crea un script que dado un usuario le de una bienvenida 
personalizada si es el administrador y da una 
bienvenida genérica si es otra persona'''

##-- Pedir al usuario que introduzca su nombre --##
name = input("Introduce tu nombre: ")

##-- Nombre del administrador --##
administrator = "Magno"

##-- Comprobar si ese nombre es igual que el del administrador --##
## Si es igual, le damos una bienveida personalizada
if(name.lower() == administrator.lower):
    print(f"¡Bienvenido, {name.title()}!")

## Si no, una bienvenida genérica
else:
    print("Bienvenido invitado genérico(NPC)")