class Carro:
    def __init__(self, color, marca, modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, incremento):
        """Aumenta la velocidad del carro."""
        self.velocidad += incremento
        print(f"El {self.marca} {self.modelo} aceleró a {self.velocidad} km/h")

    def frenar(self, decremento):
        """Disminuye la velocidad del carro."""
        self.velocidad = max(0, self.velocidad - decremento)
        print(f"El {self.marca} {self.modelo} frenó a {self.velocidad} km/h")

    def __str__(self):
        """Devuelve una representación en cadena del carro."""
        return f"Carro: {self.marca} {self.modelo}, Color: {self.color}, Velocidad: {self.velocidad} km/h"


# Ejemplo de creación y uso de un objeto Carro
mi_carro = Carro('rojo', 'Toyota', 'Corolla')

# Llamada al método __str__
print(mi_carro)  # Esto llamará automáticamente al método __str__ y mostrará la información del carro
