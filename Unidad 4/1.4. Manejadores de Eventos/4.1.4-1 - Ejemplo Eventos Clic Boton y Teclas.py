import tkinter as tk
from tkinter import messagebox

def on_button_click():
    entered_text = text_entry.get()  # Obtiene el texto del Entry
    # Muestra el texto en un Label
    display_label.config(text=entered_text)
    # Muestra el texto en la línea de comandos (CLI)
    print(entered_text)
    # Muestra el texto en una ventana de mensaje (messagebox)
    messagebox.showinfo("Información Ingresada", entered_text)

def on_enter_key(event):
    on_button_click()

def on_escape_key(event):
    root.quit()

root = tk.Tk()
root.title("Interfaz de Usuario de Demostración")
root.geometry("400x200")  # Establece un tamaño para la ventana

# Crea un Label para indicar al usuario que ingrese texto
instruction_label = tk.Label(root, text="Por favor, ingresa un texto:", font=("Arial", 14))
instruction_label.pack(pady=(10,0))

# Crea un Entry para la entrada de texto
text_entry = tk.Entry(root, font=("Arial", 14))
text_entry.pack(pady=10)

# Crea un Button que llamará a la función on_button_click cuando sea clickeado
button = tk.Button(root, text="Haz clic en mí", command=on_button_click)
button.pack(pady=(0,10))

# Crea un Label para mostrar el texto ingresado
display_label = tk.Label(root, font=("Arial", 14))
display_label.pack(pady=10)

# Vincula la tecla Enter con la función on_enter_key
root.bind('<Return>', on_enter_key)
# Vincula la tecla Escape con la función on_escape_key
root.bind('<Escape>', on_escape_key)

# Pone el foco en la entrada de texto para que el usuario pueda comenzar a escribir inmediatamente
text_entry.focus_set()

root.mainloop()
