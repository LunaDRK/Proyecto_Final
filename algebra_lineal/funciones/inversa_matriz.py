import tkinter as tk
from tkinter import messagebox
import numpy as np
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_inversa(ventana, volver_callback):
    limpiar_ventana(ventana)
    ventana.title("Inversa de Matrices")

    # Botón de regresar
    btn_volver = ttk.Button(ventana, text="← Regresar", width=15, padding=10, bootstyle="danger-outline",
                            command=volver_callback)
    btn_volver.pack(side="top", anchor="nw", padx=15, pady=15)

    # Título
    titulo = tk.Label(ventana, text="Inversa de Matrices", font=("Arial", 20, "bold"))
    titulo.pack(pady=20)

    # Frame para entrada
    frame_entrada = tk.Frame(ventana, bg="#F0F0F0")
    frame_entrada.pack(pady=10)

    tk.Label(frame_entrada, text="Ingrese la matriz (filas separadas por ';', números por espacios):", 
             font=("Arial", 14), bg="#F0F0F0").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entrada = tk.Entry(frame_entrada, width=50, font=("Arial", 12))
    entrada.grid(row=1, column=0, padx=10, pady=5)

    # Caja de texto para resultado
    resultado_text = tk.Text(ventana, width=50, height=10, wrap="word", state="disabled", bg="#F8F8F8", font=("Arial", 14))
    resultado_text.pack(pady=20)
    resultado_text.tag_configure("centrado", justify="center")

    def mostrar_resultado(texto):
        resultado_text.config(state="normal")
        resultado_text.delete("1.0", tk.END)
        resultado_text.insert(tk.END, texto, "centrado")
        resultado_text.config(state="disabled")

    # Función para calcular inversa
    def calcular():
        texto = entrada.get().strip()
        if not texto:
            messagebox.showerror("Error", "Por favor ingrese una matriz antes de calcular.")
            return
        try:
            filas = [fila.strip() for fila in texto.split(';') if fila.strip()]
            matriz = np.array([list(map(float, fila.split())) for fila in filas])

            if matriz.shape[0] != matriz.shape[1]:
                messagebox.showerror("Error", f"La matriz debe ser cuadrada")
                return

            inversa = np.linalg.inv(matriz)
            # Formato bonito con llaves como en tu multiplicación
            filas_formateadas = ["{ " + "   ".join(f"{num:6.2f}" for num in fila) + " }" for fila in inversa]
            # Dentro de la función calcular()
            texto_inversa = "\n".join(["  ".join(f"{num:8.2f}" for num in fila) for fila in inversa])
            mostrar_resultado(texto_inversa)


        except ValueError:
            messagebox.showerror("Error", "La matriz no tiene inversa'")  
        except np.linalg.LinAlgError:
            messagebox.showerror("Error", "La matriz no tiene inversa porque el determinante es 0.")
        except Exception as e:
            messagebox.showerror("Error inesperado", f"Ocurrió un problema: {e}")

    # Frame para botones
    frame_botones = ttk.Frame(ventana)
    frame_botones.pack(pady=10)

    ttk.Button(frame_botones, text="Calcular Inversa", command=calcular, padding=10, bootstyle="success-outline", width=30).pack(side=tk.LEFT, padx=10)