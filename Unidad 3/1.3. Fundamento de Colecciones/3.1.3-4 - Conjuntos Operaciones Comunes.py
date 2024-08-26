# Creación de un conjunto
frutas = {"manzana", "banana", "cereza"}

# Agregar un elemento
frutas.add("naranja")

# Eliminar un elemento
frutas.remove("banana")  # Usar discard("banana") para evitar errores si no existe

# Operaciones de conjunto
vegetales = {"tomate", "papa", "cereza"}
union = frutas | vegetales
interseccion = frutas & vegetales
diferencia = frutas - vegetales

print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia:", diferencia)
