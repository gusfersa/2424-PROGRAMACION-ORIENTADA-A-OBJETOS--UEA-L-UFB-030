import tkinter as tk
from tkinter import messagebox, Menu, scrolledtext

# Función que se ejecuta al presionar el botón
def boton_accion():
    messagebox.showinfo("Acción", "Botón presionado")

# Función para el menú desplegable
def menu_accion():
    messagebox.showinfo("Menú", "Opción del menú seleccionada")

# Función para mostrar la selección de los Radio Buttons
def mostrar_seleccion():
    messagebox.showinfo("Selección", f"Has seleccionado la opción {var_radio.get()}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Componentes GUI Comunes")
root.geometry("500x400")

# Etiqueta
etiqueta = tk.Label(root, text="Etiqueta (Label): Descripción o información")
etiqueta.pack()

# Campo de Texto
campo_texto = tk.Entry(root)
campo_texto.pack()

# Botón
boton = tk.Button(root, text="Botón: Haz clic aquí", command=boton_accion)
boton.pack()

# Casilla de Verificación
var_check = tk.IntVar()
casilla_verificacion = tk.Checkbutton(root, text="Casilla de Verificación: Opción", variable=var_check)
casilla_verificacion.pack()

# Lista Desplegable
opciones = ["Opción 1", "Opción 2", "Opción 3"]
variable_seleccionada = tk.StringVar(root)
variable_seleccionada.set(opciones[0])
lista_desplegable = tk.OptionMenu(root, variable_seleccionada, *opciones)
lista_desplegable.pack()

# Botones de Radio
var_radio = tk.StringVar()
var_radio.set("Opción 1") # Inicializa con la primera opción
radio1 = tk.Radiobutton(root, text="Opción 1", variable=var_radio, value="Opción 1", command=mostrar_seleccion)
radio1.pack()
radio2 = tk.Radiobutton(root, text="Opción 2", variable=var_radio, value="Opción 2", command=mostrar_seleccion)
radio2.pack()
radio3 = tk.Radiobutton(root, text="Opción 3", variable=var_radio, value="Opción 3", command=mostrar_seleccion)
radio3.pack()

# Área de Texto (Text Widget)
area_texto = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
area_texto.pack()

# Menú
barra_menu = Menu(root)
menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Abrir", command=menu_accion)
menu_archivo.add_command(label="Guardar", command=menu_accion)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
root.config(menu=barra_menu)

root.mainloop()
