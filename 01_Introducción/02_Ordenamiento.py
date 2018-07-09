#Recordar que lista es con corchetes

lista = [5, 4, 3, 1, 8, 6, 2]
print (lista)

#Con sorted ordenamos lo que este en lista
print (sorted(lista))

#Con reverse se aplica sorted pero al reves
print (sorted(lista, reverse = True))

#Ordenamos, pero realizando el cambio

lista.sort()
print (lista)

#Demostracion de ordenamiento con letras
lista2 = ['Ef', 'Ab', 'Gh', 'Cd']
print (sorted(lista2))