# En este ejemplo:

# La clase Vehiculo es la clase padre con atributos básicos como marca y modelo.
# La clase Coche hereda de Vehiculo y añade un atributo adicional numeroDePuertas.
# Además, tiene un método mostrar_informacion que utiliza tanto los atributos heredados
# como el atributo específico de Coche.
# Se crea un objeto mi_coche de la clase Coche y se muestra su información utilizando el
# método mostrar_informacion.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Coche(Vehiculo):  # Herencia de la clase Vehiculo
    def __init__(self, marca, modelo, numeroDePuertas):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase padre
        self.numeroDePuertas = numeroDePuertas

    # Método específico de la clase Coche
    def mostrar_informacion(self):
        return f"Coche {self.marca} {self.modelo}, con {self.numeroDePuertas} puertas"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)
        self.cilindraje = cilindraje

    def mostrar_informacion(self):
        return f"Motocicleta {self.marca} {self.modelo}, cilindraje {self.cilindraje} "

    # Creación de un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla", 4)
print(mi_coche.mostrar_informacion())

mi_motocicleta = Motocicleta("KTM","XYZ", 1200)
print((mi_motocicleta.mostrar_informacion()))