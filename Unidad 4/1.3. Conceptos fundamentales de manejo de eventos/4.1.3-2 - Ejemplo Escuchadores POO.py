import tkinter as tk
from tkinter import messagebox, scrolledtext


class CommentApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Sistema de Comentarios')
        self.master.geometry('500x250')

        # Etiqueta y campo de entrada para el nombre
        self.name_label = tk.Label(master, text='Nombre:')
        self.name_label.pack()
        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        # Etiqueta y campo de texto para el comentario
        self.comment_label = tk.Label(master, text='Comentario:')
        self.comment_label.pack()
        self.comment_text = scrolledtext.ScrolledText(master, height=5)
        self.comment_text.pack()

        # Botón para enviar el comentario
        self.submit_button = tk.Button(master, text='Enviar', command=self.submit_comment)
        self.submit_button.pack(pady=5)

        # Botón para limpiar los campos de entrada
        self.clear_button = tk.Button(master, text='Limpiar', command=self.clear_fields)
        self.clear_button.pack(pady=5)

    def submit_comment(self):
        # Recoge los valores de los campos de entrada
        name = self.name_entry.get()
        comment = self.comment_text.get("1.0", tk.END).strip()

        if name and comment:
            messagebox.showinfo("Comentario Enviado", f"Gracias {name}, tu comentario ha sido enviado.")
            self.clear_fields()
        else:
            messagebox.showwarning("Faltan Datos", "Por favor, completa todos los campos antes de enviar.")

    def clear_fields(self):
        # Limpia los campos de texto y área de texto
        self.name_entry.delete(0, tk.END)
        self.comment_text.delete('1.0', tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    app = CommentApp(root)
    root.mainloop()
