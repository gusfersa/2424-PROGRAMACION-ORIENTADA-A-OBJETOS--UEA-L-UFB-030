try:
    # Intenta abrir un archivo
    archivo = open('archivo_inexistente.txt', 'r')
except FileNotFoundError:
    print("El archivo no fue encontrado.")
else:
    # Se ejecuta si no hay excepción
    print("El archivo fue abierto exitosamente.")
    archivo.close()
finally:
    # Se ejecuta siempre, haya o no una excepción
    print("Finalizando operación de archivo.")
