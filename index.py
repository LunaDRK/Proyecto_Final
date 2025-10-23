import tkinter as tk
from algoritmos import index as algoritmos  
from matematica_discreta import index as matematicaD
from algebra_lineal import index as algebraLineal
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()


def mostrar_principal():
    limpiar_ventana()

    titulo = tk.Label(ventana, text="Seleccione un curso:", font=("Arial", 20, "bold"))
    titulo.pack(pady=100)

    btn_algoritmos = ttk.Button(ventana, text="Algoritmos", width=50, padding=20, bootstyle="warning-outline",
                               command=lambda: algoritmos.mostrar_algoritmos(ventana, mostrar_principal))
    btn_algoritmos.pack(pady=(15))

    btn_mate = ttk.Button(ventana, text="Matematica Discreta", width=50, padding=20, bootstyle="info-outline",
                               command=lambda: matematicaD.mostrar_matematica(ventana, mostrar_principal))
    btn_mate.pack(pady=15)
    
    btn_algebra = ttk.Button(ventana, text="Algebra Lineal", width=50, padding=20, bootstyle="success-outline", 
                               command=lambda: algebraLineal.mostrar_algebra(ventana, mostrar_principal))
    btn_algebra.pack(pady=15)

ventana = ttk.Window(themename="darkly")
ventana.title("Proyecto Final 2025")
#se ajusta a todas las pantallas
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
ventana.geometry(f"{screen_width}x{screen_height}+0+0")


mostrar_principal()
ventana.mainloop()
