#!/usr/bin/python3
import tkinter as tk

raiz=tk.Tk()

MAX_FILAS=3
MAX_COLUMNAS=4

for fila in range(0, MAX_FILAS):
    for columna in range(0, MAX_COLUMNAS):
        texto="Boton en ({0},{1})".format(fila, columna)
        boton=tk.Button(raiz, text=texto)
        boton.grid(row=fila, column=columna)


boton_extra=tk.Button(raiz, text="Boton en (3,1)")
boton_extra.grid(row=3, column=1, columnspan=2, sticky="e")

raiz.mainloop()