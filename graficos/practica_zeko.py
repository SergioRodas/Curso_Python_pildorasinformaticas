from tkinter import *
import tkinter.font as tkFont
import pygame
from os import path
import os, errno, sys, re

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = Tk()
root.title('Zeko sounds')

mi_frame = Frame(root, width= 650, height=700)

mi_frame.pack()

# Texto
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
texto = Label(mi_frame, text="Anasheiii guau guau", font=fontStyle, pady=20)
texto.place(x=170, y=10)

# Imagen
mi_directorio = resource_path("graficos/images/anashei.gif")
mi_imagen = PhotoImage(file=mi_directorio)
imagen_label = Label(mi_frame, image=mi_imagen).place(x=170, y=90)

# Botones
pygame.mixer.init()

def ladrar():
    pygame.mixer.music.load(resource_path("graficos/audios/ladrando.mp3"))
    pygame.mixer.music.play()

def anashei():
    pygame.mixer.music.load(resource_path("graficos/audios/anashei.mp3"))
    pygame.mixer.music.play()

mi_boton = Button(mi_frame, text="Ladrar", font=("Helvetica, 22"), command=ladrar)
mi_boton.place(x=160, y=570)

mi_boton_dos = Button(mi_frame, text="Anasheii", font=("Helvetica, 22"), command=anashei)
mi_boton_dos.place(x=300, y=570)

root.mainloop()