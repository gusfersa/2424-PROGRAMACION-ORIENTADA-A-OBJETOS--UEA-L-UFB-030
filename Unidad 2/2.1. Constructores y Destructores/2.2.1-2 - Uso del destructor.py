# "Consideremos una clase Recurso que simula la apertura y cierre
# de un recurso externo, como podría ser un archivo o una conexión de red:
class Recurso:
    def __init__(self, id):
        self.id = id
        print(f"Recurso {self.id} inicializado.")

    def __del__(self):
        print(f"Recurso {self.id} liberado.")

# "Aquí, el constructor __init__ se encarga de inicializar el objeto Recurso,
# mientras que el destructor __del__ se encarga de liberarlo.

# Al crear y eliminar instancias de Recurso, se pueden observar las acciones
# de los constructores y destructores:

mi_recurso = Recurso(1)
del mi_recurso

# La instancia mi_recurso de la clase Recurso es creada y luego eliminada.
# Esto desencadena primero el constructor y luego el destructor, gestionando
# adecuadamente la vida útil del recurso.
