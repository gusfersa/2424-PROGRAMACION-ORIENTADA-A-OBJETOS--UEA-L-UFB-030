class Carro:
    def __init__(self, modelo, anio):
        self.modelo = modelo
        self.anio = anio
        self.conductor = None  # Inicialmente, el carro no tiene conductor

    def asignar_conductor(self, persona):
        if isinstance(persona, Persona):
            self.conductor = persona

    def __str__(self):
        return f'Carro {self.modelo} del año {self.anio}, conducido por {self.conductor.nombre if self.conductor else "nadie"}.'


class Persona:
    def __init__(self, nombre, licencia):
        self.nombre = nombre
        self.licencia = licencia

    def __str__(self):
        return f'Persona {self.nombre} con licencia número {self.licencia}.'


# Creación de objetos
carro1 = Carro('Corolla', 1998)
carro2 = Carro('Blazer', 1997)
persona = Persona('Laura', 3)

# Asignar un conductor al carro
carro1.asignar_conductor(persona)

# Ejemplo de salida
print(carro1)  # Debería imprimir: Carro Corolla del año 1998, conducido por Laura.
print(carro2)  # Debería imprimir: Carro Blazer del año 1997, conducido por nadie.
print(persona)  # Debería imprimir: Persona Laura con licencia número 3.
