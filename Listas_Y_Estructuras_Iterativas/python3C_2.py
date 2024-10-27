#ENCRIPTACIÓN ROT13:

#El abecedario latino es un sistema de escritura alfabético más usado del mundo hoy en día. Se
#compone de 26 letras principales, más ciertas modificaciones y letras adicionales según el idioma
#del que se trate (por ejemplo, en castellano y gallego se incluye la ”ñ”, en portugués, francés y
#catalán la ”Ç”, en alemán la ”ß”, etc.).
#Aplicar el cifrado ROT13 a un texto se reduce a examinar sus caracteres alfabéticos y sustituirlos
#por la letra que está 13 posiciones por delante en el alfabeto, volviendo al principio si es necesario
#y conservando las mayúsculas y minúsculas: a se convierte en n, B se convierte en O, y así hasta
#la Z, que se convierte en M. Solo quedan afectadas las 26 letras principales que aparecen en el
#alfabeto latino; los números, símbolos, espacios y otros caracteres se dejan igual.
	 	 #[a,b,c,d,e,f,g,h,i,j,k,l,m] 		 	 [H, O, L, A]
 #ROT13
	 	# [n,o,p,q,r,s,t,u,v,w,x,y,z]		 	 [U, B, Y, N]

#1. Desarrolla un script que recibiendo de entrada una cadena de caracteres devuelva el texto
#codificado según el cifrado ROT13

#2. Desarrolla ahora un script que compare dos cadenas de caracteres y nos diga si una de ellas
#esta codificación ROT13 de la otra. 

def rot13(text):
	 #Tabla de traducción para cifrado ROT13
	trans = str.maketrans(
		"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
	)
	return text.translate(trans)

# Ejemplo de uso
text_1 = "Hello, Carlos."
cifrade_text = rot13(text_1)
print(cifrade_text)


#1. Desarrolla un script que recibiendo de entrada una cadena de caracteres devuelva el texto
#codificado según el cifrado ROT13

def rot13(text):
	"""
    Aplica el cifrado ROT13 a una cadena de texto.
    """
	# Tabla de traducción para cifrado ROT13
	trans = str.maketrans(
		"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
	)
	return text.translate(trans)

# Solicitar al usuario que ingrese una cadena de caracteres
user_input = input("Ingrese la cadena de texto a cifrar con ROT13: ")

# Aplicar cifrado ROT13
encoded_text = rot13(user_input)

# Mostrar el texto cifrado
print("texo cifrado con ROT13: ", encoded_text)


#2. Desarrolla ahora un script que compare dos cadenas de caracteres y nos diga si una de ellas
#esta codificación ROT13 de la otra. 

import codecs

def es_rot13(cadena1,cadena2):
	return codecs.encode(cadena1, 'rot_13') == cadena2

# Ejemplos de uso
cadena1 = "carlos richarte moreno"
cadena2 = "pneybf evpunegr zberab"
cadena3 = "Otro Texto"

print(es_rot13(cadena1, cadena2)) # Debería devolver True
print(es_rot13(cadena1, cadena3)) # Debería devolver False