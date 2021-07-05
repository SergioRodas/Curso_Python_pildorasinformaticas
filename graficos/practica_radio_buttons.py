from tkinter import *

root = Tk()

opcion = IntVar()

def imprimir():
    #print(opcion.get())
    if opcion.get() == 1:
        etiqueta.config(text="Has elegido masculino")
    elif opcion.get() == 2:
        etiqueta.config(text="Has elegido femenino")
    else:
        etiqueta.config(text="Has elegido otros")



Label(root, text="Género:").pack()

Radiobutton(root, text="Masculino", variable=opcion, value=1, command=lambda:imprimir()).pack()

Radiobutton(root, text="Femenino", variable=opcion, value=2,command=lambda:imprimir()).pack()

Radiobutton(root, text="Otros", variable=opcion, value=3,command=lambda:imprimir()).pack()

etiqueta = Label(root)
etiqueta.pack()



root.mainloop()