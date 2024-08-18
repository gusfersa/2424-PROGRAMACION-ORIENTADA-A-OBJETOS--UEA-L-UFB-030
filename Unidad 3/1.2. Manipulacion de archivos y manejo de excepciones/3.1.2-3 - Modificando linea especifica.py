# Definir la función para modificar una línea específica
def modificar_linea_archivo(nombre_archivo, numero_linea, nuevo_contenido):
    # Leer el contenido original del archivo
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.readlines()

    # Modificar la línea especificada
    contenido[numero_linea - 1] = nuevo_contenido + "\n"

    # Reescribir el archivo con la línea modificada
    with open(nombre_archivo, 'w') as archivo:
        archivo.writelines(contenido)

# Ejemplo de uso
nombre_archivo = 'ejemplo.txt'
with open(nombre_archivo, 'w') as archivo:
    archivo.write("Línea 1\n")
    archivo.write("Línea 2\n")
    archivo.write("Línea 3\n")

# Leer y mostrar el contenido original
with open(nombre_archivo, 'r') as archivo:
    print(f"\nContenido Original de {nombre_archivo}:")
    print(archivo.read())

# Modificar una línea específica y volver a imprimir
modificar_linea_archivo(nombre_archivo, 2, "Línea 2 modificada")

# Leer y mostrar el contenido modificado
with open(nombre_archivo, 'r') as archivo:
    print(f"\nContenido Modificado de {nombre_archivo}:")
    print(archivo.read())
