import tkinter as tk
from tkinter import messagebox


class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación GUI Básica")
        self.root.geometry("300x300")  # Ajusta el tamaño de la ventana a 300x300

        # Crear menú
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # Menú de archivo
        self.archivo_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.archivo_menu)
        self.archivo_menu.add_command(label="Agregar", command=self.agregar)
        self.archivo_menu.add_command(label="Limpiar", command=self.limpiar)
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label="Salir", command=self.root.quit)

        # Componentes GUI
        self.etiqueta = tk.Label(root, text="Ingrese información:")
        self.etiqueta.pack()

        self.entrada_texto = tk.Entry(root)
        self.entrada_texto.pack()

        self.boton_agregar = tk.Button(root, text="Agregar", command=self.agregar)
        self.boton_agregar.pack()

        self.boton_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.pack()

        self.lista = tk.Listbox(root)
        self.lista.pack()

    def agregar(self):
        texto = self.entrada_texto.get()
        if texto != "":
            self.lista.insert(tk.END, texto)
            self.entrada_texto.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

    def limpiar(self):
        self.lista.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()
