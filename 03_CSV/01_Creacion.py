import csv

#Usando "w" se escribe (write)
doc = open ("archivoA.csv", "w")

#Normalmente se debe dejar doc_csv_w
doc_csv_w = csv.writer(doc)

#Para trabajar archivos es super recomendable usar listas

lista = ["Roberto", 1831]

doc_csv_w.writerow(lista)

#Siempre al terminar se debe cerrar un archivo, ya que al crearse se abre
doc.close()