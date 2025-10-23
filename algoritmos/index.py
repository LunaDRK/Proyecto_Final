import tkinter as tk
from tkinter import messagebox
from algoritmos.transacciones_ventas import clientes
from algoritmos.transacciones_ventas import inventario
from algoritmos.transacciones_ventas import ventas
from algoritmos.reportes import reportes_clientes
from algoritmos.reportes import reportes_inventario
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_algoritmos(ventana, volver_callback):
    limpiar_ventana(ventana)

    # Botón de regresar
    btn_volver = ttk.Button(
        ventana, text="← Regresar", width=15, padding=10,
        bootstyle="danger-outline", command=volver_callback
    )
    btn_volver.pack(side="top", anchor="nw", padx=15, pady=15)

    # Título
    titulo = tk.Label(ventana, text="Módulo de Algoritmos", font=("Arial", 20, "bold"))
    titulo.pack(pady=35)

    # Frame para los botones
    frame_botones = ttk.Frame(ventana)
    frame_botones.pack(pady=10)

    # Botones principales
    ttk.Button(
        frame_botones, text="Clientes", width=50, padding=20, bootstyle="info-outline",
        command=lambda: clientes.mostrar_clientes(ventana, lambda: mostrar_algoritmos(ventana, volver_callback))).pack(pady=(40,15))

    ttk.Button(
        frame_botones, text="Inventario", width=50, padding=20, bootstyle="warning-outline",
        command=lambda: inventario.mostrar_inventario(
            ventana, lambda: mostrar_algoritmos(ventana, volver_callback))).pack(pady=15)

    ttk.Button(
        frame_botones, text="Ventas", width=50, padding=20, bootstyle="success-outline",
        command=lambda: ventas.mostrar_ventas(ventana, lambda: mostrar_algoritmos(ventana, volver_callback))).pack(pady=15)

    # Botones de reportes
    ttk.Button(
        frame_botones, text="Reporte de Clientes", width=50, padding=20, bootstyle="danger-outline",
            command=lambda: reportes_clientes.mostrar_reportesClientes(ventana, lambda: mostrar_algoritmos(ventana, volver_callback))).pack(pady=15)

    ttk.Button(
        frame_botones, text="Reporte de Inventario", width=50, padding=20, bootstyle="primary-outline",
        command=lambda: reportes_inventario.mostrar_reportesInventario(ventana, lambda: mostrar_algoritmos(ventana, volver_callback))).pack(pady=15)