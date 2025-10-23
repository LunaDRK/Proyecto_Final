import tkinter as tk
from tkinter import messagebox
import numpy as np
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_multiplicacion(ventana, volver_callback):
    limpiar_ventana(ventana)

    # Botón de regresar
    btn_volver = ttk.Button(ventana, text="← Regresar", width=15, padding=10, bootstyle="danger-outline",
                            command=volver_callback)
    btn_volver.pack(side="top", anchor="nw", padx=15, pady=15)

    # Título
    titulo = tk.Label(ventana, text="Multiplicación de Matrices", font=("Arial", 20, "bold"))
    titulo.pack(pady=20)

    # Frame para los Entry
    frame_entradas = tk.Frame(ventana, bg="#F0F0F0")
    frame_entradas.pack(pady=10)

    tk.Label(frame_entradas, text="Matriz A (separar filas con ';'):", font=("Arial", 14), bg="#F0F0F0").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entrada1 = tk.Entry(frame_entradas, width=40, font=("Arial", 12))
    entrada1.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_entradas, text="Matriz B (separar filas con ';'):", font=("Arial", 14), bg="#F0F0F0").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entrada2 = tk.Entry(frame_entradas, width=40, font=("Arial", 12))
    entrada2.grid(row=1, column=1, padx=10, pady=5)

    # Caja de texto para mostrar el resultado
    resultado_text = tk.Text(ventana, width=50, height=10, wrap="word", state="disabled", bg="#F8F8F8", font=("Arial", 14))
    resultado_text.pack(pady=20)
    resultado_text.tag_configure("centrado", justify="center")

    def mostrar_resultado(texto):
        resultado_text.config(state="normal")
        resultado_text.delete("1.0", tk.END)

        resultado_text.insert(tk.END, "\n" + texto, "centrado")
        resultado_text.config(state="disabled")

    # Función de cálculo
    def calcular_multiplicacion():
        try:
            texto1 = entrada1.get().strip()
            texto2 = entrada2.get().strip()

            if not texto1 or not texto2:
                messagebox.showerror("Error", "Debe ingresar ambas matrices.")
                return

            filas1 = [fila.strip() for fila in texto1.split(';') if fila.strip()]
            filas2 = [fila.strip() for fila in texto2.split(';') if fila.strip()]

            m1 = np.array([list(map(float, fila.split())) for fila in filas1])
            m2 = np.array([list(map(float, fila.split())) for fila in filas2])

            if m1.shape[1] != m2.shape[0]:
                messagebox.showerror("Error", "Matriz incompatible para multiplicación.")
                return

            producto = np.dot(m1, m2)
            texto_producto = "\n".join(["  ".join(f"{num:8.2f}" for num in fila) for fila in producto])
            mostrar_resultado(texto_producto)

        except ValueError:
            messagebox.showerror("Error", "Solo se permiten números separados por espacios.'")
        except Exception as e:
            messagebox.showerror("Error inesperado", f"Ocurrió un problema: {e}")

    # Frame para los botones
    frame_botones = ttk.Frame(ventana)
    frame_botones.pack(pady=10)

    ttk.Button(frame_botones, text="Multiplicar", command=calcular_multiplicacion, padding=10, bootstyle="success-outline", width=30).pack(side=tk.LEFT, padx=10)
