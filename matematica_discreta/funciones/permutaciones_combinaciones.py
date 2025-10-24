import tkinter as tk
from tkinter import messagebox
from scipy.special import perm, comb
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_permutacion(ventana, volver_callback):
    limpiar_ventana(ventana)

    # Boton de regresar
    btn_volver = ttk.Button(ventana, text="← Regresar", width=15, padding=10, bootstyle="danger-outline",
                           command=volver_callback)
    btn_volver.pack(side="top", anchor="nw", padx=15, pady=15)
    #titulo de la pagina
    titulo = tk.Label(ventana, text="Combinaciones y Permutaciones:", font=("Arial", 20, "bold"))
    titulo.pack(pady=40)

    #funcion para permutacion
    def permutacion():
        try:
            n = int(dato_n.get())
            r = int(dato_r.get())
            resultado = perm(n, r)
            #controlar los datos por si no hay logica
            if n < 0 or r < 0 or r > n:
                messagebox.showerror("Error", "Valores inválidos: asegúrese que r ≤ n")
                return
            formato = f"""
    {n}!
    {n}({r}) =  ------------ = {resultado}
    ({n}-{r})!
            """
            mostrar_formula(formato)
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")
    #funcion para la combi
    def combinacion():
        try:
            n = int(dato_n.get())
            r = int(dato_r.get())
            resultado = comb(n, r)
            #controlar los datos por si no hay logica
            if n < 0 or r < 0 or r > n:
                messagebox.showerror("Error", "Valores inválidos: asegúrese que r ≤ n")
                return
            formato = f"""
    {n}!
    {n}({r}) =  ------------ = {resultado}
    {r}! ({n}-{r})!
            """
            mostrar_formula(formato)
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")

    # Crear frame para los entry
    frame_nr = tk.Frame(ventana, bg="#F0F0F0")
    frame_nr.pack(pady=20)

    # entradas de datos
    tk.Label(frame_nr, text="Ingrese el dato n :", font=("Arial", 14), bg="#F0F0F0").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    dato_n = tk.Entry(frame_nr, width=20, font=("Arial", 12))
    dato_n.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame_nr, text="Ingrese el dato r:", font=("Arial", 14), bg="#F0F0F0").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    dato_r = tk.Entry(frame_nr, width=20, font=("Arial", 12))
    dato_r.grid(row=1, column=1, padx=10, pady=5)

    #caja para la formula
    pasos_text = tk.Text(ventana, width=50, height=7, wrap="word", state="disabled", bg="#F8F8F8", font=("Arial", 14))
    pasos_text.pack(pady=10)
    pasos_text.tag_configure("centrado", justify="center")

    def mostrar_formula(formato):
        pasos_text.config(state="normal")
        pasos_text.delete("1.0", tk.END)
        pasos_text.insert(tk.END, formato, "centrado")
        pasos_text.config(state="disabled")

    #botones para que esten al lado
    frame_botones = ttk.Frame(ventana)
    frame_botones.pack(pady=50)

    ttk.Button(frame_botones, text="Permutacion", command=permutacion, padding=10, bootstyle="success-outline", width=30).pack(side=tk.LEFT, padx=10)
    ttk.Button(frame_botones, text="Combinacion", command=combinacion, padding=10, bootstyle="info-outline", width=30).pack(side=tk.LEFT, padx=10)

    respu = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
    respu.pack(pady=10)

    ventana.mainloop()