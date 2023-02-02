import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
import os
from tkinter import filedialog


#Funciones para los botones

#Seleccionar Archivo y mostrarlo en la consola
def seleccionarArchivo():
    archivo = filedialog.askopenfilename(initialdir="/", title="Selecciona un archivo", filetypes=(("Excel", "*.xls"), ("Excel", "*.xlsx") , ("todos los archivos", "*.*")))

    if archivo != '':
        print(archivo)

    return archivo




class DiseñoGuiApp:
    def __init__(self, master=None, translator=None):
        _ = translator
        if translator is None:
            def _(x): return x
        # build ui
        Toplevel_1 = tk.Tk() if master is None else tk.Toplevel(master)
        Toplevel_1.configure(background="#292929", height=230, width=540)
        Toplevel_1.minsize(540, 230)
        Toplevel_1.resizable(False, False)
        Toplevel_1.title("Excel a Salary por Agustín Bustos Piasentini")
        self.Texto_de_Bienvenida = ttk.Label(Toplevel_1)
        self.Texto_de_Bienvenida.configure(
            anchor="center",
            background="#292929",
            font="{Calibri} 10 {}",
            foreground="#ffffff",
            justify="left",
            state="normal",
            takefocus=False,
            text=_('Generador de Archivos para importar al Salary por ABP'))
        self.Texto_de_Bienvenida.grid(column=1, pady=20, row=0)
        self.Seleccionar_Archivo = ttk.Button(Toplevel_1)
        self.Seleccionar_Archivo.configure(text=_('Seleccionar Archivo') , command=seleccionarArchivo)
        self.Seleccionar_Archivo.grid(column=1, row=1)
        self.Label_Periodo = ttk.Label(Toplevel_1)
        self.Label_Periodo.configure(
            background="#292929",
            font="{calibri} 8 {}",
            foreground="#ffffff",
            justify="center",
            text=_('Inserte el Período en formato MM/AA'))
        self.Label_Periodo.grid(column=1, pady=5, row=2)


        Periodo_input = tk.StringVar()

        def my_callback(var, index, mode):  
          print("Traced variable {}".format(Periodo_input.get))
        Periodo_input.trace_add("write", my_callback)

        #Hacer que el boton periodo almacele el valor del input en una variable
        def Periodo():
            Periodo = self.Input_Periodo.get()
            print(Periodo_input.get())

        self.Input_Periodo = ttk.Entry(Toplevel_1 , textvariable=Periodo_input)
        self.Input_Periodo.configure(
            cursor="xterm",
            justify="center",
            validate="all",
            width=40)
        self.Input_Periodo.grid(column=1, row=3)
        
        
        self.Boton_Periodo = ttk.Button(Toplevel_1)
        self.Boton_Periodo.configure(text=_('Seleccionar Período'))
        self.Boton_Periodo.configure(command=Periodo)
        self.Boton_Periodo.grid(column=0, pady=15, row=5)



        self.Boton_Procesar = ttk.Button(Toplevel_1)
        self.Boton_Procesar.configure(text=_('Procesar Archivo'))
        self.Boton_Procesar.grid(column=1, pady=15, row=5)
        self.Boton_Exportar = ttk.Button(Toplevel_1)
        self.Boton_Exportar.configure(text=_('Exportar Archivo'))
        self.Boton_Exportar.grid(column=3, row=5)



        #una vez que se almacenó el valor del input en la variable Periodo_input, se muestra en el label Periodo_Seleccionado

        self.Periodo_Seleccionado = ttk.Label(Toplevel_1, textvariable=Periodo_input)
        self.Periodo_Seleccionado.configure(
            background="#292929",
            font="{calibri} 8 {}",
            foreground="#999999",
            state="disabled",
            takefocus=False)
        self.Periodo_Seleccionado.grid(column=1, row=4)

        Toplevel_1.grid_propagate(0)
        Toplevel_1.grid_anchor("n")

        # Main widget
        self.mainwindow = Toplevel_1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = DiseñoGuiApp()
    app.run()
