import csv

#Usando "w" se escribe (write)
doc = open ("archivoB.csv", "w")

#Normalmente se debe dejar doc_csv_w
doc_csv_w = csv.writer(doc)

#Para trabajar archivos es super recomendable usar listas

lista = [["Roberto", 1831], ["Tito", 38], ["Yisus", 33], ["Anivia", 1]]

#Cambia de row a rows para imprimir varias listas
#De esta forma entran todos los datos de forma directa
doc_csv_w.writerows(lista)

#Siempre al terminar se debe cerrar un archivo, ya que al crearse se abre
doc.close()

'''
#Usando este for, se puede incluir un IF y filtrar los datos que se escribiran en el archivo
for x in lista:
    doc_csv_w.writerow(x)
'''