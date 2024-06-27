# Ejemplo de Buenos Identificadores en Python

# Buen identificador para una variable que almacena la cantidad de estudiantes en una clase
cantidad_estudiantes = 25

# Buen identificador para una función que crea un nuevo usuario
def crear_usuario(nombre, edad):
    nuevo_usuario = {'nombre': nombre, 'edad': edad}
    return nuevo_usuario

# Buen identificador para una variable que almacena el precio total de una compra
precio_total = 99.99

# Uso de los identificadores en un contexto de código
print(f"Cantidad de estudiantes: {cantidad_estudiantes}")
usuario = crear_usuario("Laura", 30)
print(f"Usuario creado: {usuario['nombre']} con edad {usuario['edad']}")
print(f"Precio total de la compra: {precio_total}")
