class DispositivoElectronico:
    def encender(self, modo='normal'):
        if modo == 'normal':
            return "Dispositivo electrónico encendido en modo normal"
        elif modo == 'eco':
            return "Dispositivo electrónico encendido en modo ecológico"
        else:
            return "Modo no reconocido, dispositivo electrónico encendido en modo normal"

# Creando un objeto de la clase DispositivoElectronico
mi_dispositivo = DispositivoElectronico()

# Utilizando el método con diferentes argumentos
print(mi_dispositivo.encender())  # Sin especificar modo
print(mi_dispositivo.encender('eco'))  # Modo ecológico
print(mi_dispositivo.encender('rápido'))  # Modo no reconocido
