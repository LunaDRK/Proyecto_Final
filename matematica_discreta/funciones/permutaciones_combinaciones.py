import tkinter as tk
from tkinter import messagebox
from scipy.special import perm, comb
import tkinter as tk
from tkinter import messagebox

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_permutacion(ventana, volver_callback):
    limpiar_ventana(ventana)

    # Boton de regresar
    btn_volver = tk.Button(ventana, text="Regresar", width=25, height=2, bg="#E04E4E", fg="white",
                           command=volver_callback)
    btn_volver.pack(pady=10, side='top')

    #funcion para permutacion
    def permutacion():
        try:
            n = int(dato_n.get())
            r = int(dato_r.get())
            resultado = perm(n, r)
            formato = f"""
        {n}!
    {n}({r}) =  ------------ = {resultado}
        ({n}-{r})!
            """
            respu.config(text=formato)
        except ValueError:
            print("Ingrese datos válidos")
    #funcion para la combi
    def combinacion():
        try:
            n = int(dato_n.get())
            r = int(dato_r.get())
            resultado = comb(n, r)
            formato = f"""
        {n}!
    {n}({r}) =  ------------ = {resultado}
        {r}! ({n}-{r})!
            """
            respu.config(text=formato)
        except ValueError:
            print("Ingrese datos válidos")
    # para la pantalla 

    tk.Label(ventana, text="Ingrese n:").pack(pady=5)
    dato_n = tk.Entry(ventana)
    dato_n.pack(pady=5)

    tk.Label(ventana, text="Ingrese r:").pack(pady=5)
    dato_r = tk.Entry(ventana)
    dato_r.pack(pady=5)

    tk.Button(ventana, text="Permutacion", command=permutacion, bg="#EFA00E", fg="white").pack(pady=15)
    tk.Button(ventana, text="Combinacion", command=combinacion, bg="#1D0EEF", fg="white").pack(pady=15)

    respu = tk.Label(ventana, text="", font=("Arial", 12, "bold"))
    respu.pack(pady=10)

    ventana.mainloop()
