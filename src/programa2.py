#!/usr/bin/python3
import tkinter as tk

#Ventana principal
raiz=tk.Tk()

#creamos un botón cuyo "padre" es la ventana principal
boton1=tk.Button(master=raiz, text="Soy un botón")
#En realidad, con solo un control no haría falta indicar
#ni fila ni columna
boton1.grid(row=0, column=0)
raiz.mainloop()