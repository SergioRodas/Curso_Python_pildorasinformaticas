from tkinter import *
import tkinter.font as tkFont


raiz = Tk()

# Fuentes:
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
num_fontStyle = tkFont.Font(family="Lucida Grande", size=17)

# Frame: 
mi_frame = Frame(raiz, padx=17, pady=10, bg="grey")
mi_frame.pack()

# Pantalla:
numero_pantalla = StringVar(value=0)

pantalla = Entry(mi_frame, width=17, textvariable=numero_pantalla)
pantalla.grid(row="1", column="1", padx=8, pady=18, ipadx=18, ipady=30, columnspan=4)
pantalla.config(background="black", fg="crimson", font=fontStyle ,justify="right")


# Variables globales:

operacion = ""
resultado = 0
reset_pantalla = False


# Funciones: 

#-------------------pulsaciones teclado--------------------------

def numero_pulsado(num):

	global operacion

	global reset_pantalla

	if numero_pantalla.get() == '0' or reset_pantalla != False:
		numero_pantalla.set(num)
		reset_pantalla = False
	else:
	
		numero_pantalla.set(numero_pantalla.get() + num)

	


#----------------funcion suma----------------------------------

def suma(num):

	global operacion

	global resultado

	global reset_pantalla

	if resultado == 0:
		resultado = int(num)
	else:
		resultado += int(num) #resultado=resultado+int(num)

	operacion="suma"

	reset_pantalla=True

	numero_pantalla.set(resultado)



#---------------funcion resta------------------------------
num1=0

contador_resta=0

def resta(num):

	global operacion

	global resultado

	global num1

	global contador_resta

	global reset_pantalla

	if contador_resta==0:

		num1=int(num)

		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-int(num)

		else:

			resultado=int(resultado)-int(num)	

		numero_pantalla.set(resultado)

		resultado=numero_pantalla.get()


	contador_resta=contador_resta+1

	operacion="resta"

	reset_pantalla=True


#-------------funcion multiplicacion---------------------
contador_multi=0

def multiplica(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla
	
	if contador_multi==0:

		num1=int(num)
		
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*int(num)

		else:

			resultado=int(resultado)*int(num)	

		numero_pantalla.set(resultado)
		
		resultado=numero_pantalla.get()


	contador_multi=contador_multi+1

	operacion="multiplicacion"

	reset_pantalla=True

#-----------------funcion division---------------------

contador_divi=0

def divide(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numero_pantalla.set(resultado)
		
		resultado=numero_pantalla.get()


	contador_divi=contador_divi+1

	operacion="division"

	reset_pantalla=True



#----------------funcion el_resultado----------------

def el_resultado():

	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi
	

	if operacion=="suma":

		numero_pantalla.set(resultado+int(numero_pantalla.get()))

		resultado=0

	elif operacion=="resta":

		numero_pantalla.set(int(resultado)-int(numero_pantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicacion":

		numero_pantalla.set(int(resultado)*int(numero_pantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="division":

		numero_pantalla.set(int(resultado)/int(numero_pantalla.get()))

		resultado=0

		contador_divi=0

def borrar():
    global resultado
    numero_pantalla.set(0)
    resultado = 0

# Fila 2 / Botón borrar
boton_borrar = Button(mi_frame, text=u"\u232B",  width=5, font=tkFont.Font(family="Lucida Grande", size=15), fg="red", command=lambda:borrar())
boton_borrar.grid(row=2, column=4, pady=15, ipady= 1)

# Fila 3:
boton_7 = Button(mi_frame, text="7", font=num_fontStyle, width=4, command=lambda:numero_pulsado("7"))
boton_7.grid(row=3, column=1, ipady=8)
boton_8 = Button(mi_frame, text="8", font=num_fontStyle, width=4, command=lambda:numero_pulsado("8"))
boton_8.grid(row=3, column=2, ipady=8)
boton_9 = Button(mi_frame, text="9", font=num_fontStyle, width=4, command=lambda:numero_pulsado("9"))
boton_9.grid(row=3, column=3, ipady=8)
boton_dividir = Button(mi_frame, text="÷", font=num_fontStyle, width=4)
boton_dividir.grid(row=3, column=4, ipady=8)

# Fila 4:
boton_4 = Button(mi_frame, text="4", font=num_fontStyle, width=4, command=lambda:numero_pulsado("4"))
boton_4.grid(row=4, column=1, pady=15, ipady=8)
boton_5 = Button(mi_frame, text="5", font=num_fontStyle, width=4, command=lambda:numero_pulsado("5"))
boton_5.grid(row=4, column=2, ipady=8)
boton_6 = Button(mi_frame, text="6", font=num_fontStyle, width=4, command=lambda:numero_pulsado("6"))
boton_6.grid(row=4, column=3, ipady=8)
boton_multiplicar = Button(mi_frame, text="x", font=num_fontStyle, width=4)
boton_multiplicar.grid(row=4, column=4, ipady=8)

# Fila 5:
boton_1 = Button(mi_frame, text="1", font=num_fontStyle, width=4, command=lambda:numero_pulsado("1"))
boton_1.grid(row=5, column=1, ipady=8)
boton_2 = Button(mi_frame, text="2", font=num_fontStyle, width=4, command=lambda:numero_pulsado("2"))
boton_2.grid(row=5, column=2, ipady=8)
boton_3 = Button(mi_frame, text="3", font=num_fontStyle, width=4, command=lambda:numero_pulsado("3"))
boton_3.grid(row=5, column=3, ipady=8)
boton_restar = Button(mi_frame, text="-", font=num_fontStyle, width=4, command=lambda:resta(numero_pantalla.get()))
boton_restar.grid(row=5, column=4, ipady=8)

# Fila 6:
boton_0 = Button(mi_frame, text="0", font=num_fontStyle, width=4, command=lambda:numero_pulsado("0"))
boton_0.grid(row=6, column=1, pady=15, ipady=8)
boton_coma = Button(mi_frame, text=",", font=num_fontStyle, width=4, command=lambda:numero_pulsado(","))
boton_coma.grid(row=6, column=2, ipady=8)
boton_igual = Button(mi_frame, text="=", font=num_fontStyle, width=4, command=lambda:el_resultado())
boton_igual.grid(row=6, column=3, ipady=8)
boton_suma = Button(mi_frame, text="+", font=num_fontStyle, width=4, command=lambda:suma(numero_pantalla.get()))
boton_suma.grid(row=6, column=4, ipady=8)

raiz.mainloop()