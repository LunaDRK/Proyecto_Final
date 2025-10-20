import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os
#from funciones import mcd, conjuntos, permutaciones_combinaciones
from matematica_discreta.funciones import mcd, conjuntos, permutaciones_combinaciones

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_matematica(ventana, volver_callback):
    limpiar_ventana(ventana)

    # Solo una ventana principal
    titulo = tk.Label(ventana, text="Seleccione qué quiere resolver:", font=("Arial", 16, "bold"))
    titulo.pack(pady=30)

    btn_euclides = tk.Button(ventana, text="MCD metodo de Euclides", width=25, height=2, bg="#3972AE", fg="white",
                            command=lambda: mcd.mostrar_mcd(ventana, lambda: mostrar_matematica(ventana, volver_callback)))
    btn_euclides.pack(pady=10)

    btn_matematica = tk.Button(ventana, text="Permutaciones y Combinaciones", width=25, height=2, bg="#6BDA84", fg="white",
                            command=lambda: permutaciones_combinaciones.mostrar_permutacion(ventana, lambda: mostrar_matematica(ventana, volver_callback)))
    btn_matematica.pack(pady=10)

    btn_algebra = tk.Button(ventana, text="Conjuntos", width=25, height=2, bg="#D08235", fg="white",
                            command=lambda: conjuntos.mostrar_conjuntos(ventana, lambda: mostrar_matematica(ventana, volver_callback)))
    btn_algebra.pack(pady=10)

    btn_volver = tk.Button(ventana, text="Regresar al menú principal", width=25, height=2, bg="#E04E4E", fg="white",
                           command=volver_callback)
    btn_volver.pack(pady=10)

    ventana.mainloop()