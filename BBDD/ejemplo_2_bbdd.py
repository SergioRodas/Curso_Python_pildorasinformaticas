import sqlite3

mi_conexion = sqlite3.connect("GestionProductos")

mi_cursor = mi_conexion.cursor()

# mi_cursor.execute('''
#     CREATE TABLE PRODUCTOS(
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#     PRECIO INTEGER,
#     SECCION VARCHAR(20))  
# ''')

# productos = [
#     ("pelota", 20, "jugeteria"),
#     ("pantalón", 15, "confección"),
#     ("destornillador", 25, "ferretería"),
#     ("jarrón", 45, "cerámica")
# ]

# mi_cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL, ?, ?, ?)", productos)

# mi_cursor.execute("INSERT INTO PRODUCTOS VALUES(NULL, 'tren', 15, 'juguetería')")

# LECTURA: 

mi_cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confección'")

productos = mi_cursor.fetchall()

# ACTUALIZACIÓN:

mi_cursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'pelota'")

# BORRADO:

mi_cursor.execute("DELETE FROM PRODUCTOS WHERE ID = 5")

print(productos)



mi_conexion.commit()


mi_conexion.close()