try:
    # Intenta ejecutar este bloque de código que puede lanzar excepciones
    resultado = 10 / 0  # Esto provocará un ZeroDivisionError
    #resultado = int("no es un número")  # Descomenta para probar ValueError
except ZeroDivisionError:
    print("Error: División por cero.")
except ValueError:
    print("Error: Valor no válido.")
except:
    # Captura cualquier otra excepción no capturada por los except anteriores
    print("Error desconocido.")