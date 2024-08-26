# Creación de una lista
frutas = ["manzana", "banana", "cereza"]

# Añadir un elemento
frutas.append("naranja")
frutas.pop(1, "uva")

# Acceder a un elemento
print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "uva"

# Eliminar un elemento
frutas.remove("banana")
frutas.pop(1)

# Imprimir la lista modificada
print(frutas)  # Imprime ['manzana', 'cereza', 'naranja']
