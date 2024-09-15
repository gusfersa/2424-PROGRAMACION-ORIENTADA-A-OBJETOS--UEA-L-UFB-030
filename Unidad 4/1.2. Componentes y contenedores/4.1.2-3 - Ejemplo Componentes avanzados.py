# Previo a ejecutar el programa es necesario instalar el componente tkcalendar
# Comando para instalar desde la consola o terminal
# pip install tkcalendar

import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import tkinter.messagebox as messagebox

def mostrar_fecha():
    messagebox.showinfo("Fecha Seleccionada", f"Has seleccionado: {calendario.get()}")

root = tk.Tk()
root.title("Componentes Avanzados en GUI")
root.geometry("600x500")  # Ajustado para dar espacio a las etiquetas

# Árbol (TreeView) con etiqueta
tree_label = tk.Label(root, text="TreeView - Visualización de Datos Jerárquicos")
tree_label.pack(pady=(10, 0))  # Espaciado extra en la parte superior para separar del título de la ventana

tree_frame = ttk.Frame(root)
tree_frame.pack(pady=10)

tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

mi_arbol = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
mi_arbol.pack()

tree_scroll.config(command=mi_arbol.yview)

mi_arbol['columns'] = ("Nombre", "ID")

mi_arbol.column("#0", width=0, stretch=tk.NO)
mi_arbol.column("Nombre", anchor=tk.W, width=120)
mi_arbol.column("ID", anchor=tk.CENTER, width=100)

mi_arbol.heading("#0", text="", anchor=tk.W)
mi_arbol.heading("Nombre", text="Nombre", anchor=tk.W)
mi_arbol.heading("ID", text="ID", anchor=tk.CENTER)

# Datos de ejemplo para el árbol
mi_arbol.insert(parent='', index='end', iid=0, text='', values=("Juan", "1"))
mi_arbol.insert(parent='', index='end', iid=1, text='', values=("Ana", "2"))

# Calendario (DateEntry) con etiqueta
cal_label = tk.Label(root, text="DateEntry - Selector de Fecha")
cal_label.pack(pady=(20, 0))  # Espaciado antes de la etiqueta
calendario = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
calendario.pack(pady=10)
cal_button = tk.Button(root, text="Obtener Fecha", command=mostrar_fecha)
cal_button.pack(pady=5)

# Barra de Progreso (Progressbar) con etiqueta
progress_label = tk.Label(root, text="Progressbar - Barra de Progreso")
progress_label.pack(pady=(20, 0))  # Espaciado antes de la etiqueta
progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=300, mode='determinate')
progress.pack(pady=20)
progress['value'] = 50  # Valor de ejemplo

root.mainloop()
