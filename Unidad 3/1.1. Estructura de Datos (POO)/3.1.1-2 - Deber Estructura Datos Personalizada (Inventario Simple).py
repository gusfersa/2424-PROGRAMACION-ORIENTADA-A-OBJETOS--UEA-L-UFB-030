class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)

# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()
    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '6':
            break
        elif opcion == '1':
            # Agregar producto
            pass  # Aquí se debe solicitar la información del producto al usuario y llamar a inventario.agregar_producto()
        elif opcion == '2':
            # Eliminar producto
            pass
        elif opcion == '3':
            # Actualizar producto
            pass
        elif opcion == '4':
            # Buscar producto
            pass
        elif opcion == '5':
            # Mostrar inventario
            inventario.mostrar_inventario()

if __name__ == "__main__":
    menu()
