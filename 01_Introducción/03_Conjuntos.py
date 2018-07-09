#Imprime los datos, pero como conjunto
conjunto = set ('1831')

#Se puede observar que solo muestra un 1. Y los separa en comillas
print (conjunto)

#Lo muestra como conjunto, pero realmente no lo es, ya que el 1 se repite
conjunto2 = {'1', '4', '3', '2'}
print (conjunto2)

#Interseccion (primera forma)
print (conjunto & conjunto2)
#Interseccion (segunda forma)
print (conjunto.intersection(conjunto2))