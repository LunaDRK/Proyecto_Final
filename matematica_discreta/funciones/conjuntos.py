import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_conjuntos(ventana, volver_callback):
    limpiar_ventana(ventana)

   # Boton de regresar
    btn_volver = ttk.Button(ventana, text="← Regresar", width=15, padding=10, bootstyle="danger-outline",
                           command=volver_callback)
    btn_volver.pack(side="top", anchor="nw", padx=15, pady=15)
    #titulo de la pagina
    titulo = tk.Label(ventana, text="Conjuntos", font=("Arial", 20, "bold"))
    titulo.pack(pady=40)

    #funciones para los conjuntos 
    def union():
        try:
            lista1 = lista.get().split()
            lista2 = listab.get().split()   
            a = set(lista1)
            b = set(lista2)
            resultado = sorted(a | b)
            mostrar_resultado(f"La unión es: {resultado}") 
        except Exception as error:
            messagebox.showerror("Error", f"Ocurrio: {error}")

    def interseccion():
        try:
            lista1 = lista.get().split()
            lista2 = listab.get().split()
            a = set(lista1)
            b = set(lista2)
            resultado = sorted(a & b)
            mostrar_resultado(f"La Interseccion de los conjuntos es: {resultado}")
        except Exception as error:
            messagebox.showerror("Error", f"ocurrio:, {error}")

    def diferencia():
        try:
            lista1 = lista.get().split()
            lista2 = listab.get().split()
            a = set(lista1)
            b = set(lista2)
            resultado = sorted(a - b)
            mostrar_resultado(f"la diferencia entre A - B es: {resultado}")
        except Exception as error:
            messagebox.showerror("Error", f"ocurrio", {error})

    def simetrica():
        try:
            lista1 = lista.get().split()
            lista2 = listab.get().split()
            a = set(lista1)
            b = set(lista2)
            resultado = sorted(a ^ b)
            mostrar_resultado(f"la diferencia simetrica es: {resultado}")
        except Exception as error:
            messagebox.showerror("Erro", f"ocurrio", {error})

    tk.Label(ventana, text="Ingrese los datos del primer conjunto separados por espacio:",font=("Arial", 14)).pack(pady=8)
    lista = tk.Entry(ventana, width=60,  font=("Arial", 12))
    lista.pack(pady=8, ipady=5)

    tk.Label(ventana, text="Ingrese los datos del segundo conjunto separados por espacio:",font=("Arial", 14)).pack(pady=8)
    listab = tk.Entry(ventana, width=60, font=("Arial", 12))
    listab.pack(pady=8, ipady=5)

    # Caja de texto para mostrar resultados
    respuesta_text = tk.Text(ventana, width=50, height=5, wrap="word", state="disabled", bg="#F8F8F8", font=("Arial", 14))
    respuesta_text.pack(pady=10)
    respuesta_text.tag_configure("centrado", justify="center")

    # Función para mostrar la respuesta
    def mostrar_resultado(formato):
        respuesta_text.config(state="normal")
        respuesta_text.delete("1.0", tk.END)
    
        respuesta_text.insert(tk.END, "\n" + formato, "centrado")
        respuesta_text.config(state="disabled")

    #caja de botones
    frame_botones_conjuntos = ttk.Frame(ventana)
    frame_botones_conjuntos.pack(pady=20)

    #botones para las acciones
    ttk.Button(frame_botones_conjuntos, text="Unión", command=union,
           bootstyle="success-outline", width=20, padding=10).pack(side=tk.LEFT, padx=10)

    ttk.Button(frame_botones_conjuntos, text="Intersección", command=interseccion,
           bootstyle="danger-outline", width=20, padding=10).pack(side=tk.LEFT, padx=10)

    ttk.Button(frame_botones_conjuntos, text="Diferencia A - B", command=diferencia,
           bootstyle="warning-outline", width=20, padding=10).pack(side=tk.LEFT, padx=10)

    ttk.Button(frame_botones_conjuntos, text="Diferencia simétrica", command=simetrica,
           bootstyle="info-outline", width=20, padding=10).pack(side=tk.LEFT, padx=10)

    ventana.mainloop()
