from tkinter import *
from tkinter import messagebox

root = Tk()

def info_adicional():
    messagebox.showinfo("Procesador de Sergio", "Procesador de textos versión 2021")

def aviso_licencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salir_aplicacion():
    #valor = messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")
    valor = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")

    if valor:
        root.destroy() # Cierra la aplicación

def cerrar_documento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")

    if valor:
        root.destroy()

barra_menu = Menu(root)
root.config(menu=barra_menu, width=250, height=300)

archivo_menu = Menu(barra_menu, tearoff=0)
archivo_menu.add_command(label="Nuevo Archivo")
archivo_menu.add_command(label="Guardar Archivo")
archivo_menu.add_command(label="Guardar como")
archivo_menu.add_command(label="Abrir Archivo")
archivo_menu.add_separator()
archivo_menu.add_command(label="Cerrar", command=lambda:cerrar_documento())
archivo_menu.add_command(label="Salir", command=lambda:salir_aplicacion())

archivo_edicion = Menu(barra_menu, tearoff=0)
archivo_edicion.add_command(label="Copiar")
archivo_edicion.add_command(label="Cortar")
archivo_edicion.add_command(label="Pegar")

archivo_herramientas = Menu(barra_menu, tearoff=0)

archivo_ayudas = Menu(barra_menu, tearoff=0)
archivo_ayudas.add_command(label="Licencia", command=lambda:aviso_licencia())
archivo_ayudas.add_command(label="Acerca de ...", command=lambda:info_adicional())

barra_menu.add_cascade(label="Archivo", menu=archivo_menu)
barra_menu.add_cascade(label="Edición", menu=archivo_edicion)
barra_menu.add_cascade(label="Herramientas", menu=archivo_herramientas)
barra_menu.add_cascade(label="Ayuda", menu=archivo_ayudas)




root.mainloop()