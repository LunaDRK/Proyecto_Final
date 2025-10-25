import tkinter as tk
from tkinter import messagebox
import numpy as np
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_ecuacion(ventana, volver_callback):
    limpiar_ventana(ventana)

    # Botón regresar
    btn_volver = ttk.Button(ventana, text="← Regresar", width=15, padding=10, bootstyle="danger-outline",
                                        command=volver_callback)
    btn_volver.pack(side="top", anchor="nw", padx=15, pady=15)

    # Título
    ttk.Label(ventana, text="Sistemas de Ecuaciones Lineales", font=("Arial", 20, "bold")).pack(pady=20)

    # Métodos numéricos
    def metodo_gauss_jordan(A, b):
        A = np.array(A, float)
        b = np.array(b, float)
        n = len(b)
        M = np.hstack([A, b.reshape(-1, 1)])

        for i in range(n):
            if M[i, i] == 0:
                return None
            M[i] = M[i] / M[i, i]
            for j in range(n):
                if j != i:
                    M[j] = M[j] - M[i] * M[j, i]
        return M[:, -1]

    def metodo_cramer(A, b):
        A = np.array(A, float)
        b = np.array(b, float)
        detA = np.linalg.det(A)

        if detA == 0:
            return None

        n = len(b)
        x = []
        for i in range(n):
            copia = A.copy()
            copia[:, i] = b
            detAi = np.linalg.det(copia)
            x.append(detAi / detA)

        return x

    # Método seleccionado
    opcion_metodo = tk.StringVar(value="Gauss-Jordan")
    ttk.Label(ventana, text="Método:").pack(pady=5)
    ttk.Radiobutton(ventana, text="Gauss-Jordan", variable=opcion_metodo, value="Gauss-Jordan", bootstyle="info").pack()
    ttk.Radiobutton(ventana, text="Cramer", variable=opcion_metodo, value="Cramer", bootstyle="info").pack()

    # Selección del tamaño
    ttk.Label(ventana, text="Tamaño del sistema:").pack(pady=5)
    tamano = tk.IntVar(value=2)
    opciones_menu = ttk.OptionMenu(ventana, tamano, 2, 2, 3, 4)
    opciones_menu.pack(pady=5)

    # Marco principal
    marco = ttk.Frame(ventana)
    marco.pack(pady=10)

    cajas_coef = []
    cajas_b = []

    # Crear las entradas de la matriz y vector b
    def crear_entradas():
        for w in marco.winfo_children():
            w.destroy()
        cajas_coef.clear()
        cajas_b.clear()

        n = tamano.get()

        for i in range(n):
            fila = []
            for j in range(n):
                entrada = ttk.Entry(marco, width=6, bootstyle="info")
                entrada.grid(row=i, column=j, padx=3, pady=3)
                fila.append(entrada)
            cajas_coef.append(fila)

            # Separador visual “|”
            ttk.Label(marco, text="|", font=("Arial", 12, "bold")).grid(row=i, column=n, padx=4)

            entrada_b = ttk.Entry(marco, width=6, bootstyle="info")
            entrada_b.grid(row=i, column=n + 1, padx=3)
            cajas_b.append(entrada_b)

    crear_entradas()

    # Botón actualizar tamaño
    btn_actualizar = ttk.Button(ventana, text="Actualizar tamaño", width=25, padding=10, bootstyle="info-outline", command=crear_entradas)
    btn_actualizar.pack(pady=8)

    lbl_resultado = ttk.Label(ventana, text="", font=("Arial", 12))
    lbl_resultado.pack(pady=10)

    # Resolver ecuaciones
    def resolver():
        try:
            A = []
            b = []
            for fila in cajas_coef:
                A.append([float(e.get()) for e in fila])
            for e in cajas_b:
                b.append(float(e.get()))

            A = np.array(A)
            b = np.array(b)

            detA = np.linalg.det(A)

            if detA != 0:
                if opcion_metodo.get() == "Gauss-Jordan":
                    sol = metodo_gauss_jordan(A, b)
                    if sol is None:
                        lbl_resultado.config(text="Error: pivote nulo en el método Gauss-Jordan.")
                        return
                else:
                    sol = metodo_cramer(A, b)
                    if sol is None:
                        lbl_resultado.config(text="El sistema no tiene solución única (el determinante es igual a 0).")
                        return
                # Redondear los valores
                sol = np.round(sol, 2)

                # Crear nombres de variables según el tamaño del sistema
                n = len(sol)
                variables = ['x', 'y', 'z', 'w'][:n]

                # Convertir a texto legible
                texto_sol = ', '.join(f"{var} = {val}" for var, val in zip(variables, sol))
                lbl_resultado.config(text=f"Solución única: {texto_sol}")
            else:
                rA = np.linalg.matrix_rank(A)
                rAb = np.linalg.matrix_rank(np.column_stack((A, b)))
                if rA == rAb:
                    lbl_resultado.config(text="El sistema tiene infinitas soluciones.")
                else:
                    lbl_resultado.config(text="El sistema no tiene solución.")
        except Exception as e:
            messagebox.showerror("Error", f"Verifica que todos los campos tengan números válidos.")

    # Botón resolver
    btn_resolver = ttk.Button(ventana, text="Resolver", width=25, padding=10, bootstyle="success-outline", command=resolver)
    btn_resolver.pack(pady=12)
