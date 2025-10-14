import tkinter as tk
from tkinter import messagebox

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_mcd(ventana, volver_callback):
    limpiar_ventana(ventana)

    # Boton de regresar
    btn_volver = tk.Button(ventana, text="Regresar", width=25, height=2, bg="#E04E4E", fg="white",
                           command=volver_callback)
    btn_volver.pack(pady=10, side='top')


    def euclides(a,b):
        while True:
            residuo = a % b
            if residuo == 0:
                return b
            else:
                a = b
                b = residuo
    def calcular_mcd():
        try:
            a = int(dato.get())
            b = int(datob.get())
            resultado = euclides(a, b)
            respu.config(text=f"El MCD de {a} y {b} es: {resultado}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre 0")


    ventana.title("MCD - Euclides")

    tk.Label(ventana, text="Ingrese el primer número:").pack(pady=8)
    dato = tk.Entry(ventana)
    dato.pack(pady=8)

    tk.Label(ventana, text="Ingrese el segundo número:").pack(pady=8)
    datob = tk.Entry(ventana)
    datob.pack(pady=8)

    tk.Button(ventana, text="Calcular MCD", command=calcular_mcd, bg="#EFA00E", fg="white").pack(pady=15)

    respu = tk.Label(ventana, text="", font=("Arial", 16, "bold"))
    respu.pack(pady=10)

    ventana.mainloop()
