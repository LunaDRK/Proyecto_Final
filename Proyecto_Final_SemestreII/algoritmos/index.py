import tkinter as tk
from tkinter import messagebox
from algoritmos.transacciones_ventas import clientes
from algoritmos.transacciones_ventas import inventario

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_algoritmos(ventana, volver_callback):
    limpiar_ventana(ventana)

    titulo = tk.Label(ventana, text="Módulo de Algoritmos", font=("Arial", 16, "bold"))
    titulo.pack(pady=30)

    btn_clientes = tk.Button(ventana, text="Clientes", width=25, height=2, bg="#6DD647", fg="white",
                             command=lambda: clientes.mostrar_clientes(ventana, lambda: mostrar_algoritmos(ventana, volver_callback)))
    btn_clientes.pack(pady=10)

    btn_inventario = tk.Button(ventana, text="Inventario", width=25, height=2, bg="#4E79E0", fg="white",
                              command=lambda: inventario.mostrar_inventario(ventana, lambda: mostrar_algoritmos(ventana, volver_callback)))
    btn_inventario.pack(pady=10)

    btn_volver = tk.Button(ventana, text="Regresar al menú principal", width=25, height=2, bg="#E04E4E", fg="white",
                           command=volver_callback)
    btn_volver.pack(pady=10)
