import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
#from funciones import mcd, conjuntos, permutaciones_combinaciones
from matematica_discreta.funciones import mcd, conjuntos, permutaciones_combinaciones

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_matematica(ventana, volver_callback):
    limpiar_ventana(ventana)

    # Botón de regresar
    btn_volver = ttk.Button(ventana, text="← Regresar", width=15, padding=10, bootstyle="danger-outline",
                           command=volver_callback)
    btn_volver.pack(side="top", anchor="nw", padx=15, pady=15)

    # Solo una ventana principal
    titulo = tk.Label(ventana, text="Seleccione qué quiere resolver:", font=("Arial", 20, "bold"))
    titulo.pack(pady=40)

    btn_euclides = ttk.Button(ventana, text="MCD metodo de Euclides", width=50, padding=20, bootstyle="warning-outline",
                            command=lambda: mcd.mostrar_mcd(ventana, lambda: mostrar_matematica(ventana, volver_callback)))
    btn_euclides.pack(pady=(60, 15))

    btn_matematica = ttk.Button(ventana, text="Permutaciones y Combinaciones", width=50, padding=20, bootstyle="info-outline",
                            command=lambda: permutaciones_combinaciones.mostrar_permutacion(ventana, lambda: mostrar_matematica(ventana, volver_callback)))
    btn_matematica.pack(pady=15)

    btn_algebra = ttk.Button(ventana, text="Conjuntos", width=50, padding=20, bootstyle="success-outline",
                            command=lambda: conjuntos.mostrar_conjuntos(ventana, lambda: mostrar_matematica(ventana, volver_callback)))
    btn_algebra.pack(pady=15)

    ventana.mainloop()