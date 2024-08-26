# Creación de una tupla
mi_tupla = (1, "dos", 3.0)

# Acceso a un elemento
print(mi_tupla[1])  # Imprime "dos"

# Desempaquetado de una tupla
a, b, c = mi_tupla
print(a, b, c)  # Imprime 1 dos 3.0

# Concatenación de tuplas
nueva_tupla = mi_tupla + (4, 5)
print(nueva_tupla)  # Imprime (1, 'dos', 3.0, 4, 5)
