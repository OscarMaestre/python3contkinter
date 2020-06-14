#!/usr/bin/python3
 
from tkinter import *




class GUI(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.raiz=master
        self.crear_variables()
        self.crear_controles()
        self.configurar_pesos_rejilla()
        self.configurar_eventos()        

    def crear_variables(self):
        self.valor_deslizador=IntVar(name="valordeldeslizador")
        self.valor_deslizador.set(1500)

        self.texto_entry=StringVar()
    
    def crear_controles(self):
        self.deslizador=Scale(master=raiz, from_=100, to=200, 
                orient=HORIZONTAL, variable=self.valor_deslizador)

        self.deslizador.grid(row=0, column=0,sticky="nsew")

        self.valor=Entry(master=raiz, textvariable=self.texto_entry)
        self.valor.grid(row=0, column=1,sticky="nsew")

    def configurar_pesos_rejilla(self):
        self.raiz.grid_rowconfigure(0, weight=1)

        self.raiz.grid_columnconfigure(0, weight=4)
        self.raiz.grid_columnconfigure(1, weight=1)

    


    def configurar_eventos(self):
        self.valor_deslizador.trace("w", self.on_change_valor_deslizador)
        

    def on_change_valor_deslizador(self, nombrevariable, indicelista, operacion):
        self.texto_entry.set(self.valor_deslizador.get())
    


raiz=Tk()
interfaz=GUI(master=raiz)
raiz.mainloop()