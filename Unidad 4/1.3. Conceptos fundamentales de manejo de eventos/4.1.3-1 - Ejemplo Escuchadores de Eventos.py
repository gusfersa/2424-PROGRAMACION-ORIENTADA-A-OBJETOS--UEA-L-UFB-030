import tkinter as tk
from tkinter import messagebox

def on_save_clicked():
    # Aquí se ejecutaría la lógica de guardar los datos
    # Por ejemplo, guardar los datos en un archivo o en una base de datos
    # Para este ejemplo, simplemente mostraremos un messagebox
    messagebox.showinfo("Guardar", "Los datos han sido guardados correctamente.")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Escuchadores de Eventos")
root.geometry("300x150")

# Crear un botón y registrar el escuchador de eventos para el evento de clic
save_button = tk.Button(root, text="Guardar", command=on_save_clicked)
save_button.pack(pady=20)

# Iniciar el bucle principal de la GUI
root.mainloop()
