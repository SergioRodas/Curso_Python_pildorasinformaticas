from tkinter import *
from tkinter import filedialog

root = Tk()

def abre_fichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Solo imágenes .gif", "*.gif"), ("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))
    print(fichero)

Button(root, text="Abrir fichero", command=lambda:abre_fichero()).pack()


root.mainloop()