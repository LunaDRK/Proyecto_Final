import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_conjuntos(ventana, volver_callback):
    limpiar_ventana(ventana)

    # Boton de regresar
    btn_volver = tk.Button(ventana, text="Regresar", width=25, height=2, bg="#E04E4E", fg="white",
                           command=volver_callback)
    btn_volver.pack(pady=10, side='top')

    #funciones para los conjuntos 
    def union():
        try:
            lista1 = lista.get().split()
            lista2 = listab.get().split()   
            a = set(lista1)
            b = set(lista2)
            resultado = sorted(a | b)
            respuesta.config(text=f"La unión es: {resultado}")
        except Exception as error:
            messagebox.showerror("Error", f"Ocurrio: {error}")

    def interseccion():
        try:
            lista1 = lista.get().split()
            lista2 = listab.get().split()
            a = set(lista1)
            b = set(lista2)
            resultado = sorted(a & b)
            respuesta.config(text=f"La Interseccion de los conjuntos es: {resultado}")
        except Exception as error:
            messagebox.showerror("Error", f"ocurrio:, {error}")

    def diferencia():
        try:
            lista1 = lista.get().split()
            lista2 = listab.get().split()
            a = set(lista1)
            b = set(lista2)
            resultado = sorted(a - b)
            respuesta.config(text=f"la diferencia entre A - B es: {resultado}")
        except Exception as error:
            messagebox.showerror("Error", f"ocurrio", {error})

    def simetrica():
        try:
            lista1 = lista.get().split()
            lista2 = listab.get().split()
            a = set(lista1)
            b = set(lista2)
            resultado = sorted(a ^ b)
            respuesta.config(text=f"la diferencia simetrica es: {resultado}")
        except Exception as error:
            messagebox.showerror("Erro", f"ocurrio", {error})

    tk.Label(ventana, text="Ingrese los datos del primer conjunto separados por espacio:").pack(pady=8)
    lista = tk.Entry(ventana, width=60)
    lista.pack(pady=8)

    tk.Label(ventana, text="Ingrese los datos del segundo conjunto separados por espacio:").pack(pady=8)
    listab = tk.Entry(ventana, width=60)
    listab.pack(pady=8)

    #botones para las funciones
    tk.Button(ventana, text="Unión", command=union, bg="#1BAA54", fg="white",
            font=("Arial", 12, "bold")).pack(pady=15)

    tk.Button(ventana, text="Interseccion", command=interseccion, bg="#C22348", fg="white",
            font=("Arial", 12, "bold")).pack(pady=15)

    tk.Button(ventana, text="Diferencia A - B", command=diferencia, bg="#EB1EB5", fg="white",
            font=("Arial", 12, "bold")).pack(pady=15)

    tk.Button(ventana, text="Diferencia simetrica", command=simetrica, bg="#B0CC10", fg="white",
            font=("Arial", 12, "bold")).pack(pady=15)

    respuesta = tk.Label(ventana, text="", font=("Arial", 16, "bold"))
    respuesta.pack(pady=10)

    ventana.mainloop()
