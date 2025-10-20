import tkinter as tk
from tkinter import messagebox
from algoritmos import index as algoritmos  
from matematica_discreta import index as matematicaD
from algebra_lineal import index as algebraLineal

def limpiar_ventana():
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_principal():
    limpiar_ventana()

    titulo = tk.Label(ventana, text="Seleccione un curso:", font=("Arial", 16, "bold"))
    titulo.pack(pady=30)

    btn_algoritmos = tk.Button(ventana, text="Algoritmos", width=25, height=2, bg="#3972AE", fg="white",
                               command=lambda: algoritmos.mostrar_algoritmos(ventana, mostrar_principal))
    btn_algoritmos.pack(pady=10)

    btn_mate = tk.Button(ventana, text="Matematica Discreta", width=25, height=2, bg="#6BDA84", fg="white",
                               command=lambda: matematicaD.mostrar_matematica(ventana, mostrar_principal))
    btn_mate.pack(pady=10)
    
    btn_algebra = tk.Button(ventana, text="Algebra Lineal", width=25, height=2, bg="#D08235", fg="white",
                               command=lambda: algebraLineal.mostrar_algebra(ventana, mostrar_principal))
    btn_algebra.pack(pady=10)

ventana = tk.Tk()
ventana.title("Proyecto Final 2025")
ventana.geometry("800x500")

mostrar_principal()
ventana.mainloop()
