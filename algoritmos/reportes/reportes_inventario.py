import tkinter as tk
from tkinter import ttk, messagebox
import openpyxl
import os

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_reportesInventario(ventana, volver_callback):
    limpiar_ventana(ventana)

    # Boton de regresar
    btn_volver = tk.Button(ventana, text="Regresar", width=25, height=2, bg="#E04E4E", fg="white",
                           command=volver_callback)
    btn_volver.pack(pady=10, side='top')

    titulo = tk.Label(ventana, text="Reportes de Inventario", font=("Arial", 18, "bold"))
    titulo.pack(pady=15, side='top')

# Tabla
    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(pady=10)

    columnas = ("Producto", "Total Vendido", "Unidades Vendidas")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=12)
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=350, anchor="center")
    tabla.pack()