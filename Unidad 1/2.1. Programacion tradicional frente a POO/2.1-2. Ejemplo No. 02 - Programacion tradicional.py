# Programación Tradicional
# Ejemplo: Gestión de un vehículo

# Definición de variables globales
fuel_tank = 0
mileage = 0
fuel_efficiency = 25

# Función para llenar el tanque de combustible
def fill_tank(amount):
    global fuel_tank
    fuel_tank += amount

# Función para conducir el vehículo
def drive(distance):
    global fuel_tank, mileage, fuel_efficiency
    fuel_needed = distance / fuel_efficiency
    if fuel_needed <= fuel_tank:
        fuel_tank -= fuel_needed
        mileage += distance
        print("Driving:", distance, "miles")
    else:
        print("Not enough fuel to drive that far.")

# Uso de las funciones en la programación tradicional
fill_tank(20)
drive(100)

# Imprimir la distancia recorrida y el nivel de combustible restante
print("Mileage (Traditional):", mileage)
print("Fuel Tank (Traditional):", fuel_tank)