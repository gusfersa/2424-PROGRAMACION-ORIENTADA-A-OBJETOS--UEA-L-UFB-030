class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id_producto] = producto

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto.nombre, producto.precio)

# Ejemplo de uso
inventario = Inventario()
inventario.agregar_producto(Producto(1, "Teclado", 19.99))
inventario.agregar_producto(Producto(2, "Mouse", 9.99))
inventario.mostrar_inventario()
