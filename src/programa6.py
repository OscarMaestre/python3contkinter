#!/usr/bin/python3
import tkinter as tk

raiz=tk.Tk()

MAX_FILAS=3
MAX_COLUMNAS=4

#Creamos nuestra matriz de botones
for fila in range(0, MAX_FILAS):
    for columna in range(0, MAX_COLUMNAS):
        texto="Boton en ({0},{1})".format(fila, columna)
        boton=tk.Button(raiz, text=texto)
        boton.grid(row=fila, column=columna, sticky="nsew", padx=0, pady=0)


raiz.geometry("600x600")
raiz.grid_rowconfigure(0, weight=2)
raiz.grid_rowconfigure(1, weight=6)
raiz.grid_rowconfigure(2, weight=2)

raiz.grid_columnconfigure(0, weight=2)
raiz.grid_columnconfigure(1, weight=4)
raiz.grid_columnconfigure(2, weight=2)
raiz.grid_columnconfigure(3, weight=2)

raiz.mainloop()