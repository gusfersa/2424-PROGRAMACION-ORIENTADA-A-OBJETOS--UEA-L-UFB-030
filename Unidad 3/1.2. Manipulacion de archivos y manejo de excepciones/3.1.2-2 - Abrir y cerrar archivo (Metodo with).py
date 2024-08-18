# Usando 'with' para abrir el archivo en modo lectura.
with open('ejemplo_lectura.txt', 'r') as archivo:
    print(archivo.read())  # Imprime el contenido del archivo

# Usando 'with' para abrir el archivo en modo escritura (creándolo si no existe).
# Escribe en él y luego se cierra automáticamente.
with open('ejemplo_escritura.txt', 'w') as archivo:
    archivo.write('Este es un nuevo archivo.')  # Escribe en el archivo

# Usando 'with' para abrir el archivo en modo añadir.
# Añade una nueva línea y luego se cierra automáticamente.
with open('ejemplo_escritura.txt', 'a') as archivo:
    archivo.write('\nAñadiendo una segunda línea.')  # Añade nueva línea de texto

# Usando 'with' para abrir el archivo en modo lectura.
with open('ejemplo_escritura.txt', 'r') as archivo:
    print(archivo.read())  # Imprime el contenido del archivo