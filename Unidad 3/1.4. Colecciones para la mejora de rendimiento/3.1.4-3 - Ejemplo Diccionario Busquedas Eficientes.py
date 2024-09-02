class Empleado:
    def __init__(self, id_empleado, nombre, departamento):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.departamento = departamento

    def __str__(self):
        return f"{self.id_empleado}: {self.nombre}, Departamento: {self.departamento}"

class GestionEmpleados:
    def __init__(self):
        # Inicializar un diccionario vacío para almacenar objetos Empleado
        self.empleados = {}

    def agregar_empleado(self, empleado):
        # La clave es el ID del empleado, facilitando una búsqueda rápida
        self.empleados[empleado.id_empleado] = empleado

    def eliminar_empleado(self, id_empleado):
        if id_empleado in self.empleados:
            del self.empleados[id_empleado]
            print(f"Empleado {id_empleado} eliminado con éxito.")
        else:
            print("Empleado no encontrado.")

    def buscar_empleado(self, id_empleado):
        # Acceso directo al empleado mediante su ID
        return self.empleados.get(id_empleado, "Empleado no encontrado.")

    def mostrar_empleados(self):
        for empleado in self.empleados.values():
            print(empleado)

# Ejemplo de uso
gestion = GestionEmpleados()
gestion.agregar_empleado(Empleado("001", "Juan Pérez", "Recursos Humanos"))
gestion.agregar_empleado(Empleado("002", "Ana Gómez", "Finanzas"))

print("Búsqueda de empleado por ID:")
print(gestion.buscar_empleado("001"))
print(gestion.buscar_empleado("003"))  # ID inexistente

print("\nListado completo de empleados:")
gestion.mostrar_empleados()

# Eliminar un empleado y mostrar el listado actualizado
gestion.eliminar_empleado("001")
print("\nListado después de eliminar un empleado:")
gestion.mostrar_empleados()
