import tkinter as tk
from tkinter import ttk, messagebox

def on_enter_pressed_in_entry(event):
    # Agregar el texto del cuadro de entrada al Treeview
    text = text_entry.get()
    if text:
        treeview.insert('', tk.END, values=(text,))
        text_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa texto antes de presionar Enter.")

def on_escape_pressed(event):
    messagebox.showinfo("Evento de Tecla", "Tecla Escape presionada. Cerrando aplicación.")
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo Avanzado de Manejo de Eventos de Teclado")
root.geometry("400x300")

# Instrucciones
instructions = tk.Label(root, text="Ingresa texto y presiona Enter para agregar al listado:\nPresiona Escape para cerrar la aplicación.",
                        justify=tk.CENTER, font=('Arial', 12))
instructions.pack(pady=10)

# Cuadro de entrada de texto
text_entry = tk.Entry(root)
text_entry.pack(pady=10)
text_entry.focus()  # Poner el foco en el cuadro de entrada

# Treeview para mostrar los textos agregados
treeview = ttk.Treeview(root, columns=('Text'), show='headings')
treeview.heading('Text', text='Textos Ingresados')
treeview.pack(pady=10, fill=tk.BOTH, expand=True)

# Vincular evento de tecla Enter solo al cuadro de texto
text_entry.bind('<Return>', on_enter_pressed_in_entry)

# Vincular evento de tecla Escape a la ventana principal
root.bind('<Escape>', on_escape_pressed)

root.mainloop()
