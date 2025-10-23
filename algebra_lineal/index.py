import tkinter as tk
from tkinter import messagebox
from algebra_lineal.funciones import multiplicacion_matrices, inversa_matriz, ecuaciones_lineales
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_algebra(ventana, volver_callback):
    limpiar_ventana(ventana)
    # Botón de regresar
    btn_volver = ttk.Button(ventana, text="← Regresar", width=15, padding=10, bootstyle="danger-outline",
                           command=volver_callback)
    btn_volver.pack(side="top", anchor="nw", padx=15, pady=15)

    # Solo una ventana principal
    titulo = tk.Label(ventana, text="Seleccione qué quiere resolver:", font=("Arial", 20, "bold"))
    titulo.pack(pady=40)
    #botones
    btn_multiplicacion = ttk.Button(ventana, text="Multiplicacion de Matrices", width=50, padding=20, bootstyle="warning-outline",
                            command=lambda: multiplicacion_matrices.mostrar_multiplicacion(ventana, lambda: mostrar_algebra(ventana, volver_callback)))
    btn_multiplicacion.pack(pady=(60,15))

    btn_inversa = ttk.Button(ventana, text="Inversa de Matrices", width=50,padding=20, bootstyle="info-outline",
                            command=lambda: inversa_matriz.mostrar_inversa(ventana, lambda: mostrar_algebra(ventana, volver_callback)))
    btn_inversa.pack(pady=15)

    btn_ecuaciones = ttk.Button(ventana, text="Ecuaciones Lineales", width=50,padding=20, bootstyle="success-outline",
                            command=lambda: ecuaciones_lineales.mostrar_ecuacion(ventana, lambda: mostrar_algebra(ventana, volver_callback)))
    btn_ecuaciones.pack(pady=15)
