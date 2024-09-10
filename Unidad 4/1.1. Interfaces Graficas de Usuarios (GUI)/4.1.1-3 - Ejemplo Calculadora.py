import tkinter as tk

def agregar_caracter(caracter):
    entrada.insert(tk.END, caracter)

def calcular(*args):
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
        log.config(text=f"Operación: {expresion}, Resultado: {resultado}")
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")
        log.config(text="Error")

def limpiar():
    entrada.delete(0, tk.END)
    log.config(text="")

def salir():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x300")

# Centrar la ventana en la pantalla
ancho_ventana = ventana.winfo_reqwidth()
alto_ventana = ventana.winfo_reqheight()
posicion_derecha = int(ventana.winfo_screenwidth() / 2 - ancho_ventana / 2)
posicion_abajo = int(ventana.winfo_screenheight() / 2 - alto_ventana / 2)
ventana.geometry("+{}+{}".format(posicion_derecha, posicion_abajo))

# Crear un menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Limpiar", command=limpiar)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# Crear un campo de entrada
entrada = tk.Entry(ventana, font=("Arial", 18), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entrada.bind("<Return>", calcular)
entrada.bind("<Escape>", lambda event: limpiar())

# Crear un label para visualizar las operaciones en formato de log
log = tk.Label(ventana, text="", font=("Arial", 12))
log.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

# Crear los botones de los números
numeros = "7894561230"
for i, num in enumerate(numeros):
    tk.Button(ventana, text=num, font=("Arial", 14), command=lambda num=num: agregar_caracter(num)).grid(row=(i//3)+2, column=(i%3), padx=5, pady=5)

# Botón para el punto decimal
tk.Button(ventana, text=".", font=("Arial", 14), command=lambda: agregar_caracter(".")).grid(row=5, column=1, padx=5, pady=5)

# Botón para el cálculo
tk.Button(ventana, text="=", font=("Arial", 14), command=calcular).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Crear los botones de las operaciones
operadores = ["+", "-", "*", "/"]
for i, operador in enumerate(operadores):
    tk.Button(ventana, text=operador, font=("Arial", 14), command=lambda op=operador: agregar_caracter(op)).grid(row=i+2, column=3, padx=5, pady=5)

# Ejecutar el bucle de eventos
ventana.mainloop()
