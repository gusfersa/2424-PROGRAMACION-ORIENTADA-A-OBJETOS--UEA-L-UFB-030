import tkinter as tk
from tkinter import messagebox

def calcular_resultado():
    try:
        # Obtiene el valor del campo de entrada y realiza un cálculo
        numero = float(entrada.get())
        resultado = numero * 2
        # Muestra el resultado en el área de texto
        area_texto.insert(tk.END, f"El doble de {numero} es {resultado}\n")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido.")

# Función para limpiar el área de texto
def limpiar_resultado():
    area_texto.delete(1.0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Software de Cálculo del Doble")
ventana.geometry("400x400")

# Crear un menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Crear una opción de menú "Archivo" con una opción "Salir"
menu_archivo = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Crear un título
titulo = tk.Label(ventana, text="Calcula el doble de un número")
titulo.pack(pady=10)

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Introduce un número:")
etiqueta.pack()

# Crear un campo de entrada
entrada = tk.Entry(ventana)
entrada.pack()

# Crear un botón para calcular el resultado
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_resultado)
boton_calcular.pack(pady=5)

# Crear un botón para limpiar el resultado
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_resultado)
boton_limpiar.pack(pady=5)

# Crear un área de texto para mostrar el resultado
area_texto = tk.Text(ventana, height=10, width=30)
area_texto.pack()

# Ejecutar el bucle de eventos
ventana.mainloop()