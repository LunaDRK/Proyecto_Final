import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_mcd(ventana, volver_callback):
    limpiar_ventana(ventana)
    ventana.title("MCD - Método de Euclides")

    # Botón de regresar
    btn_volver = ttk.Button(ventana, text="← Regresar", width=15, padding=10, bootstyle="danger-outline",
                           command=volver_callback)
    btn_volver.pack(side="top", anchor="nw", padx=15, pady=15)
    #titolo de la pagina
    titulo = tk.Label(ventana, text="MCD metodo de Euclides:", font=("Arial", 20, "bold"))
    titulo.pack(pady=40)

    frame_mcd = tk.Frame(ventana, bg="#F0F0F0")
    frame_mcd.pack(pady=20)

    tk.Label(frame_mcd, text="Ingrese el primer número   :", font=("Arial", 14), bg="#F0F0F0").grid(row=0, column=0, padx=10, pady=8, sticky="e")
    dato = tk.Entry(frame_mcd, width=40, font=("Arial", 12))
    dato.grid(row=0, column=1, padx=10, pady=8)

    tk.Label(frame_mcd, text="Ingrese el segundo número:", font=("Arial", 14), bg="#F0F0F0").grid(row=1, column=0, padx=10, pady=8, sticky="e")
    datob = tk.Entry(frame_mcd, width=40, font=("Arial", 12))
    datob.grid(row=1, column=1, padx=10, pady=8)

    # Área donde se mostrarán los pasos
    pasos_text = tk.Text(ventana, width=50, height=10, wrap="word", state="disabled", bg="#F8F8F8", font=("Arial", 16))
    pasos_text.pack(pady=10)

    # Label para el resultado final
    respu = tk.Label(ventana, text="", font=("Arial", 14, "bold"))
    respu.pack(pady=10)

    def mostrar_paso(texto):
        pasos_text.config(state="normal")
        pasos_text.insert(tk.END, texto + "\n")
        pasos_text.config(state="disabled")
        pasos_text.see(tk.END)

    def euclides_pasos(a, b):
        pasos = []
        while b != 0:
            residuo = a % b
            pasos.append(f"{a} = {b} x {a // b} + {residuo}")
            a, b = b, residuo
        return pasos, a  # a es el MCD

    def calcular_mcd():
        pasos_text.config(state="normal")
        pasos_text.delete("1.0", tk.END)
        pasos_text.config(state="disabled")
        respu.config(text="")

        try:
            a = int(dato.get())
            b = int(datob.get())
            if b == 0:
                raise ZeroDivisionError

            pasos, resultado = euclides_pasos(a, b)
            for paso in pasos:
                mostrar_paso(paso)
            respu.config(text=f"El MCD de {a} y {b} es: {resultado}")

        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre 0")

    ttk.Button(ventana, text="Calcular MCD", command=calcular_mcd, width=50,
              padding=20, bootstyle="success-outline").pack(pady=15)

    ventana.mainloop()
