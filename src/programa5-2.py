#!/usr/bin/python3
import tkinter as tk

raiz=tk.Tk()

MAX_FILAS=3
MAX_COLUMNAS=4

for fila in range(0, MAX_FILAS):
    for columna in range(0, MAX_COLUMNAS):
        texto="Boton en ({0},{1})".format(fila, columna)
        boton=tk.Button(raiz, text=texto)
        #Usamos sticky para que el botón aproveche 
        #todo el espacio sobrante
        boton.grid(row=fila, column=columna, sticky="nsew")

#Ahora asignamos el mismo peso a todas las filas 
for fila in range(0, MAX_FILAS):
    raiz.grid_rowconfigure(fila, weight=1)

#Y configuramos también el peso de las columnas
for columna in range(0, MAX_COLUMNAS):
    raiz.grid_columnconfigure(columna, weight=1)
raiz.mainloop()