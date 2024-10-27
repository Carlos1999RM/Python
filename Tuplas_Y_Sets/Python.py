# Tuplas
# mi_tupla_1 = ("fruta", 45, True)
# print(type(mi_tupla_1))

# Espacio en memoria lista vs tupla
import sys
mi_lista = [0,1,2, "hola", True]
mi_tupla = [0,1,2, "hola", True]
#print(sys.getsizeof(mi_lista), "bytes")
#print(sys.getsizeof(mi_tupla), "bytes")

# Print the Python version
#print("Python version")
#print(sys.version)
#print("Version info.")
#print(sys.version_info)

tupla1 = (25,23,26)
tupla2 = ('Carlos','Guillermo', 'Joaquín')
tuple3 = ('Jerez de la frontera','Jerez de la frontera','Jerez de la frontera')
tupla_combinada = tuple(zip(tupla2, tupla1, tuple3))
#print(tupla_combinada)

# Sintaxis de los set
set_fruta = {'manzana', 'naranja', 'melón'}
#print(set_fruta)