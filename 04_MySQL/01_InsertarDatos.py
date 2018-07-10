import mysql.connector

con = mysql.connector.connect(user = "root", password = "", host = "127.0.0.1", database = "bdpython")

cursor = con.cursor()

#Crea la tabla (lo comente desp de crearla)
#cursor.execute("CREATE TABLE example (id INT, data VARCHAR(100));")

#Con esto insertamos datos en la tabla
cursor.execute("INSERT INTO example (id, data) VALUES ('9', 'dato')")

#Con esto se almacenan los datos creados (commit)
con.commit()

con.close()
