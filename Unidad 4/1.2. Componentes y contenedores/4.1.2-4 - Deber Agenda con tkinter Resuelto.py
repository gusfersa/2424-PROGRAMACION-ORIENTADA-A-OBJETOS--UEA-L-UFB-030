import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame para los campos de entrada
        self.entry_frame = ttk.Frame(self.root)
        self.entry_frame.pack(pady=20)

        # Selector de fecha
        self.date_label = ttk.Label(self.entry_frame, text="Fecha:")
        self.date_label.grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.entry_frame, width=15, background='darkblue', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        # Campo de entrada para la hora
        self.time_label = ttk.Label(self.entry_frame, text="Hora:")
        self.time_label.grid(row=0, column=2, padx=5, pady=5)
        self.time_entry = ttk.Entry(self.entry_frame, width=15)
        self.time_entry.grid(row=0, column=3, padx=5, pady=5)

        # Campo de entrada para la descripción
        self.desc_label = ttk.Label(self.entry_frame, text="Descripción:")
        self.desc_label.grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = ttk.Entry(self.entry_frame, width=50)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # Botón para agregar evento
        self.add_button = ttk.Button(self.entry_frame, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=2, column=1, padx=5, pady=5)

        # Botón para eliminar evento seleccionado
        self.delete_button = ttk.Button(self.entry_frame, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.delete_button.grid(row=2, column=2, padx=5, pady=5)

        # TreeView para mostrar los eventos
        self.tree = ttk.Treeview(self.root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.pack(pady=20)

        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        # Botón para salir de la aplicación
        self.exit_button = ttk.Button(self.root, text="Salir", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def add_event(self):
        # Obtiene los valores de los campos de entrada
        date = self.date_entry.get()
        time = self.time_entry.get()
        description = self.desc_entry.get()

        # Añade el evento al TreeView
        self.tree.insert("", tk.END, values=(date, time, description))

        # Limpia los campos de entrada
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def delete_event(self):
        # Obtiene el evento seleccionado
        selected_item = self.tree.selection()[0]
        self.tree.delete(selected_item)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
