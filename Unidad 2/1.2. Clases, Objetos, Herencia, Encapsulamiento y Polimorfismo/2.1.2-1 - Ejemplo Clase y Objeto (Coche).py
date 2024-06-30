# Aquí hay un ejemplo simple de cómo definir una clase en Python:

class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} color {self.color} está arrancando.")

    def informacion(self):
        print(f"Datos Informativos del coche: {self.marca} {self.modelo} color {self.color}.")


# En este ejemplo, Coche es la clase con atributos marca, modelo, y color, y un método arrancar().

# Creación de Objetos:

# A partir de esta clase, podemos crear múltiples objetos, cada uno representando un coche específico
# con sus propias características.

mi_coche = Coche("Suzuki", "SZ", "Gris")
mi_coche.arrancar()

coche_luis = Coche("KIA", "Sportage", "Azul")
coche_luis.informacion()
