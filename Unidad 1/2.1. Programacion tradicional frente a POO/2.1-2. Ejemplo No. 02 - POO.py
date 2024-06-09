# Programación Orientada a Objetos (POO)
# Ejemplo: Gestión de un vehículo

class Vehicle:
    def __init__(self, fuel_efficiency=25):
        self.fuel_tank = 0
        self.mileage = 0
        self.fuel_efficiency = fuel_efficiency

    def fill_tank(self, amount):
        self.fuel_tank += amount

    def drive(self, distance):
        fuel_needed = distance / self.fuel_efficiency
        if fuel_needed <= self.fuel_tank:
            self.fuel_tank -= fuel_needed
            self.mileage += distance
            print("Driving:", distance, "miles")
        else:
            print("Not enough fuel to drive that far.")

# Crear una instancia de la clase Vehicle
car = Vehicle()

# Uso de los métodos en la programación orientada a objetos
car.fill_tank(20)
car.drive(100)

# Imprimir la distancia recorrida y el nivel de combustible restante
print("Mileage (OOP):", car.mileage)
print("Fuel Tank (OOP):", car.fuel_tank)