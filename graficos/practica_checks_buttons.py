from tkinter import *

root = Tk()

root.title("Ejemplo")

playa = IntVar()
montania = IntVar()
turismo_rural = IntVar() 

def opciones_viaje():
    opcion_escogida = ""
    
    if playa.get() == 1:
        opcion_escogida += "Playa.  "
    
    if montania.get() == 1:
        opcion_escogida += "Montaña.  "
    
    if turismo_rural.get() == 1:
        opcion_escogida += "Turismo rural."

    texto_final.config(text="Destinos elegidos: \n" + opcion_escogida)

foto = PhotoImage(file="graficos/images/avion.gif")
Label(root, image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Elige destinos:", width="50").pack()

Checkbutton(frame, text="Playa", variable= playa, onvalue=1, offvalue=0, command=lambda:opciones_viaje()).pack()
Checkbutton(frame, text="Montaña", variable= montania, onvalue=1, offvalue=0, command=lambda:opciones_viaje()).pack()
Checkbutton(frame, text="Turismo rural", variable= turismo_rural, onvalue=1, offvalue=0, command=lambda:opciones_viaje()).pack()

texto_final = Label(frame)
texto_final.pack()


root.mainloop()