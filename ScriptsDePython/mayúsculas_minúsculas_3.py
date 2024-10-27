
# Pedir datos al usuario
letra = input("Introduce una letra: ")
# Mayúsculas 65 -- 90
# Minúaculas 97 -- 122

if 65 <= ord(letra) <=90:
    print("La tiene es mayúculas")
elif 97 <= ord(letra) <= 122:
    print("La letra es minúculas")
else:
    print("La letra introducida no es válida")