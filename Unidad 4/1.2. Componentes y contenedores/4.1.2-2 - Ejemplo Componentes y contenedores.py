import tkinter as tk
from tkinter import ttk, messagebox, Menu, scrolledtext

def boton_accion():
    messagebox.showinfo("Acción", "Botón presionado")

def menu_accion():
    messagebox.showinfo("Menú", "Opción del menú seleccionada")

def mostrar_seleccion():
    messagebox.showinfo("Selección", f"Has seleccionado la opción {var_radio.get()}")

def combobox_seleccion(event):
    seleccion = combobox.get()
    messagebox.showinfo("Lista Desplegable", f"Has seleccionado: {seleccion}")

root = tk.Tk()
root.title("Componentes GUI Comunes")
root.geometry("700x500")  # Ajustado para acomodar todos los componentes

# Panel para Controles de Entrada con borde, fondo y título
panel_entrada = tk.Frame(root, borderwidth=2, relief="groove", bg="light gray")
panel_entrada.pack(padx=10, pady=5, fill=tk.X)
titulo_entrada = tk.Label(panel_entrada, text="Controles de Entrada", bg="light gray")
titulo_entrada.pack(side=tk.TOP, fill=tk.X)

# Componentes del panel de entrada
etiqueta = tk.Label(panel_entrada, text="Etiqueta (Label): Descripción o información", bg="light gray")
etiqueta.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
campo_texto = tk.Entry(panel_entrada)
campo_texto.pack(side=tk.TOP, fill=tk.X, padx=5)

# Lista desplegable (Combobox)
opciones_combobox = ["Opción 1", "Opción 2", "Opción 3"]
combobox = ttk.Combobox(panel_entrada, values=opciones_combobox)
combobox.current(0)  # Establece la selección predeterminada a la primera opción
combobox.bind("<<ComboboxSelected>>", combobox_seleccion)
combobox.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

# Panel para Botones y Selección con borde, fondo y título
panel_botones = tk.Frame(root, borderwidth=2, relief="groove", bg="light blue")
panel_botones.pack(padx=10, pady=5, fill=tk.X)
titulo_botones = tk.Label(panel_botones, text="Botones y Selección", bg="light blue")
titulo_botones.pack(side=tk.TOP, fill=tk.X)

# Componentes del panel de botones
boton = tk.Button(panel_botones, text="Botón: Haz clic aquí", command=boton_accion)
boton.pack(side=tk.LEFT, padx=5, pady=5)

var_check = tk.IntVar()
casilla_verificacion = tk.Checkbutton(panel_botones, text="Casilla de Verificación: Opción", variable=var_check, bg="light blue")
casilla_verificacion.pack(side=tk.LEFT, padx=5)

var_radio = tk.StringVar()
var_radio.set("Opción 1")  # Inicializa con la primera opción
radio1 = tk.Radiobutton(panel_botones, text="Opción 1", variable=var_radio, value="Opción 1", command=mostrar_seleccion, bg="light blue")
radio1.pack(side=tk.LEFT, padx=5)
radio2 = tk.Radiobutton(panel_botones, text="Opción 2", variable=var_radio, value="Opción 2", command=mostrar_seleccion, bg="light blue")
radio2.pack(side=tk.LEFT, padx=5)
radio3 = tk.Radiobutton(panel_botones, text="Opción 3", variable=var_radio, value="Opción 3", command=mostrar_seleccion, bg="light blue")
radio3.pack(side=tk.LEFT, padx=5)

# Panel para Área de Texto con borde, fondo y título
panel_texto = tk.Frame(root, borderwidth=2, relief="groove", bg="light green")
panel_texto.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
titulo_texto = tk.Label(panel_texto, text="Área de Texto", bg="light green")
titulo_texto.pack(side=tk.TOP, fill=tk.X)

# Área de texto
area_texto = scrolledtext.ScrolledText(panel_texto, wrap=tk.WORD)
area_texto.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

# Configuración de Menú
barra_menu = Menu(root)
menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Abrir", command=menu_accion)
menu_archivo.add_command(label="Guardar", command=menu_accion)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
root.config(menu=barra_menu)

root.mainloop()
