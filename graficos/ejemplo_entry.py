from tkinter import *

raiz = Tk()

mi_frame = Frame(raiz, width=1200, height=600)

mi_frame.pack()

mi_nombre = StringVar()

        # Entrys:

cuadro_nombre = Entry(mi_frame, textvariable=mi_nombre)
cuadro_nombre.grid(row=0, column=1, padx=25)
cuadro_nombre.config(justify="center")

cuadro_apellido = Entry(mi_frame)
cuadro_apellido.grid(row=1, column=1, padx=25)
cuadro_apellido.config(justify="center")

cuadro_direccion = Entry(mi_frame)
cuadro_direccion.grid(row=2, column=1, padx=25)
cuadro_direccion.config(justify="center")

cuadro_contrasenia = Entry(mi_frame)
cuadro_contrasenia.grid(row=3, column=1, padx=25)
cuadro_contrasenia.config(justify="center", show="*")

texto_comentario = Text(mi_frame, width=16, height=5)
texto_comentario.grid(row=4, column=1, padx=25, pady=10)

scroll_comentario = Scrollbar(mi_frame, command=texto_comentario.yview)
scroll_comentario.grid(row=4, column=1, pady=10, sticky="nse")

texto_comentario.config(yscrollcommand=scroll_comentario.set)

         # Labels:

nombre_label = Label(mi_frame, text="Nombre:")
nombre_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

apellido_label = Label(mi_frame, text="Apellido:")
apellido_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

direccion_label = Label(mi_frame, text="Dirección:")
direccion_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

direccion_label = Label(mi_frame, text="Contraseña:")
direccion_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)

comentarios_label = Label(mi_frame, text="Comentarios:")
comentarios_label.grid(row=4, column=0, sticky="e", padx=10, pady=10)

def codigo_boton():
        mi_nombre.set("Sergio")

boton_envio = Button(raiz, text="Enviar", command=codigo_boton)
boton_envio.pack()

raiz.mainloop()