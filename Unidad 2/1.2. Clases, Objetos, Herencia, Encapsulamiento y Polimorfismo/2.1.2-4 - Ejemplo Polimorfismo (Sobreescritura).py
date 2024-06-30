class DispositivoElectronico:
    def encender(self):
        return "Dispositivo electrónico encendido"

class Telefono(DispositivoElectronico):
    def encender(self):
        return "Teléfono iniciado y listo para usar"

class Computadora(DispositivoElectronico):
    def encender(self):
        return "Computadora arrancando, bienvenido"

# Creando objetos de las clases derivadas
mi_telefono = Telefono()
mi_computadora = Computadora()

# Utilizando el método sobrescrito
print(mi_telefono.encender())
print(mi_computadora.encender())

# En este código:

# La clase DispositivoElectronico tiene un método encender, que
# proporciona un mensaje genérico de encendido.

# Las clases Telefono y Computadora heredan de DispositivoElectronico
# y sobrescriben el método encender para proporcionar mensajes
# específicos para cada tipo de dispositivo.

# Al crear instancias de Telefono y Computadora y llamar al método
# encender, se ejecutan las versiones sobrescritas de este método,
# demostrando polimorfismo.