# Ejemplo de Convenciones de Nomenclatura en Python

# Clases: CamelCase (cada palabra comienza con mayúscula)
class VehiculoElectrico:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_informacion(self):
        return f"Vehículo Eléctrico: {self.marca} {self.modelo}"

# Funciones y variables: snake_case (palabras separadas por guiones bajos)
def calcular_distancia(rendimiento, energia):
    return rendimiento * energia

# Constantes: MAYUSCULAS con guiones bajos
MAX_ENERGIA = 100

# Instancia de la clase
mi_tesla = VehiculoElectrico("Tesla", "Model 3")

# Llamada a función
distancia = calcular_distancia(3.5, MAX_ENERGIA)

print(mi_tesla.mostrar_informacion())
print(f"Distancia máxima posible: {distancia} km")
