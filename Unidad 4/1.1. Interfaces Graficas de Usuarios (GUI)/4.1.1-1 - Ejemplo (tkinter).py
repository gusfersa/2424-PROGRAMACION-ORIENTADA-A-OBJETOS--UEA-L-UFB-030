import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "Hola, esto es un mensaje de prueba.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de GUI con Tkinter")
ventana.geometry('400x400')

# Crear un botón
boton = tk.Button(ventana, text="Mostrar mensaje", command=mostrar_mensaje)
boton.pack(pady=20)

# Ejecutar el bucle de eventos
ventana.mainloop()
