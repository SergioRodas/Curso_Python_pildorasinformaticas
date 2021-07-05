from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import sqlite3



# Raíz:
root = Tk()
root.geometry("373x505")

# Pantalla:
id_pantalla = StringVar()
nombre_pantalla = StringVar()
apellido_pantalla = StringVar()
contrasenia_pantalla = StringVar()
direccion_pantalla = StringVar()
comentario_pantalla = "" 


# Funciones:
def conectar_bbdd():
    try:
        mi_conexion = sqlite3.connect("Usuarios")
        mi_cursor = mi_conexion.cursor()
        mi_cursor.execute('''
        CREATE TABLE DATOS_USUARIOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR(50),
        APELLIDO VARCHAR(50),
        CONTRASENIA VARCHAR(50),
        DIRECCION VARCHAR(50),
        COMENTARIOS VARCHAR(200)
        )
        ''')
        mi_conexion.close()
        messagebox.showinfo("BBDD","BBDD creada con éxito.")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe.")


def salir_aplicacion():
    valor = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")

    if valor:
        root.destroy() # Cierra la aplicación

def borrar_campos():
    entrada_id.delete(0, 'end')
    entrada_nombre.delete(0, 'end')
    entrada_apellido.delete(0, 'end')
    entrada_contrasenia.delete(0, 'end')
    entrada_direccion.delete(0, 'end')
    texto_comentario.delete("1.0", 'end')

def guardar_texto_comentario():
    global comentario_pantalla
    comentario_pantalla = texto_comentario.get("1.0","end")

def insertar_texto_comentario(texto):
    texto_comentario.delete(1.0,"end")
    texto_comentario.insert(1.0, texto)

def crear_usuario():
    global comentario_pantalla
    guardar_texto_comentario()
    mi_conexion = sqlite3.connect("Usuarios")
    mi_cursor = mi_conexion.cursor()
    mi_cursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, ?, ?, ?, ?, ?)", (nombre_pantalla.get(), apellido_pantalla.get(), contrasenia_pantalla.get(), direccion_pantalla.get(), comentario_pantalla))

    mi_conexion.commit()
    mi_conexion.close()
    messagebox.showinfo("BBDD","Registro creado con éxito.")
    


def leer_usuario():
    global comentario_pantalla

    try:
        mi_conexion = sqlite3.connect("Usuarios")
        mi_cursor = mi_conexion.cursor()
        mi_cursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID = {}".format(id_pantalla.get()))
        usuario = mi_cursor.fetchall()
        datos_usuario = usuario[0]
        nombre_pantalla.set(datos_usuario[1])
        apellido_pantalla.set(datos_usuario[2])
        contrasenia_pantalla.set(datos_usuario[3])
        direccion_pantalla.set(datos_usuario[4])
        insertar_texto_comentario(datos_usuario[5])

        mi_conexion.commit()
        mi_conexion.close()
    except:
        messagebox.showerror("Error", "No existe un usuario que coincida con la id ingresada.")

def actualizar_usuario():
    global comentario_pantalla
    guardar_texto_comentario()
    mi_conexion = sqlite3.connect("Usuarios")
    mi_cursor = mi_conexion.cursor()

    mi_cursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO = ?, APELLIDO = ?, CONTRASENIA = ?, DIRECCION = ?, COMENTARIOS = ? WHERE ID = ?", (nombre_pantalla.get(), apellido_pantalla.get(), contrasenia_pantalla.get(), direccion_pantalla.get(), comentario_pantalla, id_pantalla.get()))

    mi_conexion.commit()
    mi_conexion.close()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito.")

def borrar_usuario():
    mi_conexion = sqlite3.connect("Usuarios")
    mi_cursor = mi_conexion.cursor()

    mi_cursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID = ?", (id_pantalla.get()))

    mi_conexion.commit()
    mi_conexion.close()
    messagebox.showinfo("BBDD", "Registro borrado con éxito.")


def aviso_licencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def info_adicional():
    messagebox.showinfo("Manejo de base de datos", "Interfaz para manejar la base de datos 'Usuarios'. Versión 2021") 



# Fuentes:
fontStyle = tkFont.Font(family="Lucida Grande", size=10)

# Marco:
mi_frame = Frame(root)
mi_frame.pack()

# Menú:
menu_bar = Menu(root)
root.config(menu=menu_bar)

bbdd = Menu(menu_bar, tearoff=0)
bbdd.add_command(label="Conectar", command=lambda:conectar_bbdd())
bbdd.add_separator()
bbdd.add_command(label="Salir", command=lambda:salir_aplicacion())

borrar = Menu(menu_bar, tearoff=0)
borrar.add_command(label="Borrar campos", command=lambda:borrar_campos())

crud = Menu(menu_bar, tearoff=0)
crud.add_command(label="Crear", command=lambda:crear_usuario())
crud.add_command(label="Leer", command=lambda:leer_usuario())
crud.add_command(label="Actualizar", command=lambda:actualizar_usuario())
crud.add_command(label="Borrar", command=lambda:borrar_usuario())

ayuda = Menu(menu_bar, tearoff=0)

ayuda.add_command(label="Licencia", command=lambda:aviso_licencia())
ayuda.add_command(label="Acerca de...", command=lambda:info_adicional())

menu_bar.add_cascade(label="          BBDD        ", menu=bbdd)
menu_bar.add_cascade(label="      Borrar      ", menu=borrar)
menu_bar.add_cascade(label="       CRUD       ", menu=crud)
menu_bar.add_cascade(label="        Ayuda        ", menu=ayuda)

# Entradas:
entrada_id = Entry(mi_frame, justify="center", width=30, textvariable=id_pantalla)
entrada_id.grid(row=0, column=3, pady=30, padx=5)

entrada_nombre = Entry(mi_frame, justify="center", width=30, textvariable=nombre_pantalla)
entrada_nombre.grid(row=1, column=3)

entrada_apellido = Entry(mi_frame, justify="center", width=30, textvariable=apellido_pantalla)
entrada_apellido.grid(row=2, column=3, pady=30)

entrada_contrasenia = Entry(mi_frame, justify="center", width=30, textvariable=contrasenia_pantalla, show="*")
entrada_contrasenia.grid(row=3, column=3)

entrada_direccion = Entry(mi_frame, justify="center", width=30, textvariable=direccion_pantalla)
entrada_direccion.grid(row=4, column=3, pady=30)

texto_comentario = Text(mi_frame, width=22, height=9)
texto_comentario.grid(row=5, column=3)

scroll_comentario = Scrollbar(mi_frame, command=texto_comentario.yview)
scroll_comentario.grid(row=5, column=4, sticky="nse")

texto_comentario.config(yscrollcommand=scroll_comentario.set)

# Etiquetas:
etiqueta_id = Label(mi_frame, text="ID:")
etiqueta_id.config(font=fontStyle)
etiqueta_id.grid(row=0, column=0, sticky="e", padx=30)

etiqueta_nombre = Label(mi_frame, text="Nombre:")
etiqueta_nombre.config(font=fontStyle)
etiqueta_nombre.grid(row=1, column=0, sticky="e", padx=30)

etiqueta_apellido = Label(mi_frame, text="Apellido:")
etiqueta_apellido.config(font=fontStyle)
etiqueta_apellido.grid(row=2, column=0, sticky="e", padx=30)

etiqueta_contrasenia = Label(mi_frame, text="Contraseña:")
etiqueta_contrasenia.config(font=fontStyle)
etiqueta_contrasenia.grid(row=3, column=0, sticky="e", padx=30)

etiqueta_direccion = Label(mi_frame, text="Dirección:")
etiqueta_direccion.config(font=fontStyle)
etiqueta_direccion.grid(row=4, column=0, sticky="e", padx=30)

etiqueta_comentarios = Label(mi_frame, text="Comentarios:")
etiqueta_comentarios.config(font=fontStyle)
etiqueta_comentarios.grid(row=5, column=0, sticky="e", padx=30)

# Botones:
boton_crear = Button(root, text="   Crear  ", command=lambda:crear_usuario())
boton_crear.place(x=25, y=460)

boton_leer = Button(root, text="   Leer   ", command=lambda:leer_usuario())
boton_leer.place(x=110, y=460)

boton_actualizar = Button(root, text="Actualizar", command=lambda:actualizar_usuario())
boton_actualizar.place(x=198, y=460)

boton_borrar = Button(root, text="  Borrar  ", command=lambda:borrar_usuario())
boton_borrar.place(x=293, y=460)








root.mainloop()
