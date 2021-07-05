import sqlite3

mi_conexion = sqlite3.connect("PrimeraBase")

mi_cursor = mi_conexion.cursor()

#mi_cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#mi_cursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',    15, 'DEPORTES')")

# varios_productos = [
#     ("Camiseta", 10, "Deportes"),
#     ("Jarrón", 90, "Cerámica"),
#     ("Camión", 20, "Juguetería")
# ]

# mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", varios_productos)

mi_cursor.execute("SELECT * FROM PRODUCTOS")

varios_productos = mi_cursor.fetchall()

for producto in varios_productos:
    print("Nombre de artículo:", producto[0], "\nSección:", producto[2], "\nPrecio:", producto[1], "\n")


mi_conexion.commit()


mi_conexion.close()