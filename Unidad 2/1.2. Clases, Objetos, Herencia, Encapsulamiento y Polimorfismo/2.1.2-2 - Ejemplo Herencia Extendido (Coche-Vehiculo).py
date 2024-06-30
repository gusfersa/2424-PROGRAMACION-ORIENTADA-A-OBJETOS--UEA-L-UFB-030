class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_identificacion(self):
        return f"Vehículo de marca {self.marca}, modelo {self.modelo}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, numeroDePuertas):
        super().__init__(marca, modelo)
        self.numeroDePuertas = numeroDePuertas

    def mostrar_detalles(self):
        informacion_base = super().mostrar_identificacion()
        return f"{informacion_base}, con {self.numeroDePuertas} puertas"

# Creando un objeto de la clase Vehiculo
mi_vehiculo = Vehiculo("Toyota", "Corolla")
print(mi_vehiculo.mostrar_identificacion())

# Creando un objeto de la clase Coche
mi_coche = Coche("Honda", "Civic", 4)
print(mi_coche.mostrar_detalles())
