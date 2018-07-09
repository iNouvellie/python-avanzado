print ('\n' *50)

#Creación de una cadena simple
cadena = "Hola mundo ? Roberto ? Juan ? Pedro"

#Reemplazo de una palabra o texto de una cadena
nueva = cadena.replace('Hola', 'HOLA')

#Imprime el lugar donde esta lo que buscamos
print (cadena.find("l"))

#Imprime la cadena nueva
print (nueva)

#Elimina los espacios al inicio o final, no intermedios
otramas = cadena.strip()

print (cadena)
print (otramas)

#Para quitar en particular el inicial lstrip, final rstrip

#Todo mayus o minus
ma = cadena.upper()
me = cadena.lower()
print (ma)
print (me)
print (cadena.split("?"))