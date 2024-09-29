import tkinter as tk

def on_left_click(event):
    instructions.config(text="Clic izquierdo detectado.")

def on_right_click(event):
    instructions.config(text="Clic derecho detectado.")

def on_middle_click(event):
    instructions.config(text="Clic de scroll detectado.")

def on_mouse_enter(event):
    event.widget.config(bg='lightblue')

def on_mouse_leave(event):
    event.widget.config(bg='SystemButtonFace')

def on_mouse_move(event):
    position_label.config(text=f"Posición del mouse: x={event.x}, y={event.y}")

root = tk.Tk()
root.title("Monitor de Eventos de Teclado y Mouse")
root.geometry("500x400")

instructions = tk.Label(root, text="Instrucciones:\n"
                                   "Clic izquierdo: Detecta clic izquierdo del mouse.\n"
                                   "Clic derecho: Detecta clic derecho del mouse.\n"
                                   "Clic de scroll: Detecta clic con la rueda del mouse.\n"
                                   "Mueve el mouse sobre este texto para ver su posición.",
                        justify=tk.LEFT)
instructions.pack(pady=10)

# Vinculación de eventos de clic del mouse
instructions.bind("<Button-1>", on_left_click)
instructions.bind("<Button-2>", on_middle_click)
instructions.bind("<Button-3>", on_right_click)

# Vinculación de eventos de movimiento del mouse
instructions.bind("<Enter>", on_mouse_enter)
instructions.bind("<Leave>", on_mouse_leave)
root.bind("<Motion>", on_mouse_move)

# Label para mostrar la posición del mouse
position_label = tk.Label(root, text="Posición del mouse: x=0, y=0")
position_label.pack(pady=10)

root.mainloop()
