import tkinter as tk
from tkinter import messagebox

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_mcd(ventana, volver_callback):
    limpiar_ventana(ventana)
    ventana.title("MCD - Método de Euclides")

    # Botón de regresar
    btn_volver = tk.Button(ventana, text="Regresar", width=25, height=2, bg="#E04E4E", fg="white",
                           command=volver_callback)
    btn_volver.pack(pady=10, side='top')

    # Etiquetas y campos de entrada
    tk.Label(ventana, text="Ingrese el primer número:").pack(pady=8)
    dato = tk.Entry(ventana)
    dato.pack(pady=8)

    tk.Label(ventana, text="Ingrese el segundo número:").pack(pady=8)
    datob = tk.Entry(ventana)
    datob.pack(pady=8)

    # Área donde se mostrarán los pasos
    pasos_text = tk.Text(ventana, width=50, height=10, wrap="word", state="disabled", bg="#F8F8F8")
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

    tk.Button(ventana, text="Calcular MCD", command=calcular_mcd,
              bg="#EFA00E", fg="white", width=20, height=2).pack(pady=15)

    ventana.mainloop()

