from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

# raiz.resizable(0,0) # bool

raiz.iconbitmap("graficos/images/Kenny2.ico")

raiz.geometry("650x350")

raiz.config(bg="orange")

raiz.config(bd=40)

raiz.config(relief="groove")

raiz.config(cursor="hand2")

mi_frame = Frame()

mi_frame.pack()

mi_frame.config(bg="white")

mi_frame.config(width="620", height="335")

mi_frame.config(bd=25)

mi_frame.config(relief="groove")

mi_frame.config(cursor="pirate")

raiz.mainloop()

