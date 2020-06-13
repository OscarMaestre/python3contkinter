#!/usr/bin/python3
import tkinter as tk

#Ventana principal
raiz=tk.Tk()

MAX_FILAS=3
MAX_COLUMNAS=4

for fila in range(0, MAX_FILAS):
    for columna in range(0, MAX_COLUMNAS):
        #Se crea un boton y se indica a ese boton
        #que se posiciones en una cierta fila y columna
        texto="Boton en ({0},{1})".format(fila, columna)
        boton=tk.Button(raiz, text=texto)
        boton.grid(row=fila, column=columna)

raiz.mainloop()