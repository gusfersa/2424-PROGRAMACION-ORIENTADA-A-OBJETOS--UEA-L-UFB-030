try:
    # Intenta ejecutar este bloque de código
    resultado = 10 / 0
except ZeroDivisionError:
    # Captura y maneja la excepción ZeroDivisionError
    print("Error: División por cero no permitida.")
else:
    # Este bloque se ejecuta si no hay excepciones en el bloque try
    print("División realizada exitosamente.")
finally:
    # Este bloque se ejecuta siempre, haya o no una excepción
    print("Operación de división finalizada.")
