class Punto:
    def __init__(self, x, y):
        self.coordenadas = (x, y)

    def mostrar_coordenadas(self):
        print(f"X: {self.coordenadas[0]}, Y: {self.coordenadas[1]}")


# Ejemplo de uso
punto = Punto(10, 20)
punto.mostrar_coordenadas()
