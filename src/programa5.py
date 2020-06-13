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

#Ahora asignamos el mismo peso a todas las filas 
#y ningún peso a las columnas.
for fila in range(0, MAX_FILAS):
    raiz.grid_rowconfigure(fila, weight=1)

raiz.mainloop()