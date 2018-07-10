import mysql.connector

con = mysql.connector.connect(user = "root", password = "", host = "127.0.0.1", database = "bdpython")

#Creamos cursor
cursor = con.cursor()

#Sintaxis para leer dato
cursor.execute("SELECT * FROM 'example' WHERE 'id' = 9")

#Como no sabemos cuantos item leera y regresara, hacemos row
#Rows es todo lo que regresa

rows = cursor.fetchall()

for row in rows:
    print (row)

cursor.close()
con.close()