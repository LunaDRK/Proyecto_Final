import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import tkinter.simpledialog as simpledialog
from email.message import EmailMessage
import smtplib, ssl, mimetypes, os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

SERVIDOR = "smtp.gmail.com"
PUERTO = 587
CONTRASENA = os.getenv('GOOGLE_APP_PASS')
USUARIO = os.getenv("GOOGLE_EMAIL")

def limpiar_ventana(ventana):
    for widget in ventana.winfo_children():
        widget.destroy()

def mostrar_reportesInventario(ventana, volver_callback):
    limpiar_ventana(ventana)

     # Botón de regresar
    btn_volver = ttk.Button(ventana, text="← Regresar", width=15, padding=10,bootstyle="danger-outline", command=volver_callback)
    btn_volver.pack(side="top", anchor="nw", padx=15, pady=15)

    # Título
    titulo = tk.Label(ventana, text="Reportes de inventario", font=("Arial", 20, "bold"))
    titulo.pack(pady=10)

    ARCHIVO = "algoritmos/transacciones_ventas/proyecto.xlsx"
    productos = pd.read_excel(ARCHIVO, sheet_name='Inventario')
    ventas = pd.read_excel(ARCHIVO, sheet_name='Ventas')

    # Asegurar consistencia de nombres de columnas
    productos.columns = productos.columns.str.strip().str.title()
    ventas.columns = ventas.columns.str.strip().str.title()

    # Agrupar ventas por producto
    reporte = ventas.groupby('Codigo Producto').agg(
        Veces_Vendido=('Cantidad', 'count'),
        Total_Ventas=('Total', 'sum')
    ).reset_index()

    # Unir con la lista de productos para obtener el nombre
    reporte = pd.merge(reporte, productos, left_on='Codigo Producto', right_on='Codigo', how='left')
    reporte = reporte.fillna({
    "Codigo Cliente": "—",
    "Nombre": "—",
    "Numero_Compras": 0,
    "Total_Gastado": 0.0
    })

    # Seleccionar columnas finales
    reporte_final = reporte[['Nombre', 'Veces_Vendido', 'Total_Ventas']]

    # Crear tabla en tkinter
    columnas = ("Producto", "Veces vendido", "Total en ventas")
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=200, anchor="center")
    tabla.pack(expand=True, fill="both", padx=10, pady=10)
    tabla.place(width=700, height=500 , anchor='center' , relx=0.5, rely=0.5)

    # Insertar datos en la tabla
    for _, fila in reporte_final.iterrows():
        tabla.insert("", "end", values=(fila["Nombre"], fila["Veces_Vendido"], fila["Total_Ventas"]))

    # Guardar reporte en un archivo Excel
    ruta_reporte = "algoritmos/reportes/Reporte_Inventario.xlsx"
    reporte_final.to_excel(ruta_reporte, index=False)

    # Función para enviar correo
    def solicitar_envio_correo():
        correo = simpledialog.askstring("Enviar por correo", "Ingrese el correo de destino:")
        if not correo:
            messagebox.showwarning("Error", "Ingresa un correo electrónico")
            return
        
        enviar_reporte(
            asunto="Reporte de Inventario",
            cuerpo="Adjunto el reporte de ventas por producto generado por el sistema de ventas",
            destinatario=correo,
            titulo="Reporte de Inventario",
            nombre_archivo="Reporte_Inventario.xlsx",
            ruta_de_adjunto="algoritmos/reportes"
        )

    #boton para enviar reporte
    btn_enviar = ttk.Button(text="Enviar Reporte", width=25, padding=10, bootstyle="info-outline",
                            command=solicitar_envio_correo)
    btn_enviar.pack(pady=15, side='bottom')

#Funcion para enviar el reporte de inventario por correo
def enviar_reporte(asunto, cuerpo, destinatario, titulo, nombre_archivo, ruta_de_adjunto):
    try:
        # Contenido del mensaje
        mensaje = EmailMessage()
        mensaje["Subject"] = asunto
        mensaje["From"] = USUARIO
        mensaje["To"] = destinatario
        mensaje.set_content(cuerpo)
        mensaje.add_alternative(f"<h1>{titulo}</h1><p>{cuerpo}</p>", subtype="html")

        # Adjuntar archivo
        ctype, encoding = mimetypes.guess_type(nombre_archivo)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"
        tipo_principal, sub_tipo = ctype.split("/", 1)

        with open(os.path.join(ruta_de_adjunto, nombre_archivo), "rb") as archivo:
            mensaje.add_attachment(archivo.read(), maintype=tipo_principal, subtype=sub_tipo, filename=nombre_archivo)

        # Enviar el mensaje
        context = ssl.create_default_context()
        with smtplib.SMTP(SERVIDOR, PUERTO) as smtp:
            smtp.starttls(context=context)
            smtp.login(USUARIO, CONTRASENA)
            smtp.send_message(mensaje)
        messagebox.showinfo("Éxito", f"El reporte ha sido enviado exitosamente al correo {destinatario}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo enviar el correo.\nError: {str(e)}")