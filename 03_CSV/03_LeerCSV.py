import csv

#La letra r, es de lectura
#La letra a, append, concatenar
#La letra w, es sobre escribir o crear

doc = open ("archivoB.csv","r")

doc_csv = csv.reader(doc)

for (nombre, numero) in doc:
#Deberia usarse print nombre, numero segun el curso, pero hay problemas
    print (nombre, numero)

doc.close()

#Hay un error en el for del read, asociado a la version 3 y no 2 de Python que se esta utilizando