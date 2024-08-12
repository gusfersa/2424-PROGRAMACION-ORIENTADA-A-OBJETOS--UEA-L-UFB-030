# Definición de la clase Contacto
# Esta clase modela un contacto individual con nombre, teléfono y email.
class Contacto:
    # Constructor de la clase con tres parámetros: nombre, teléfono y email
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre  # Asigna el nombre del contacto
        self.telefono = telefono  # Asigna el teléfono del contacto
        self.email = email  # Asigna el email del contacto

# Definición de la clase Agenda
# Esta clase maneja una colección de contactos.
class Agenda:
    # Constructor de la clase Agenda
    # Inicializa la lista de contactos como vacía
    def __init__(self):
        self.contactos = []  # Lista para almacenar los objetos de tipo Contacto

    # Método para agregar un nuevo contacto a la agenda
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)  # Añade el objeto contacto a la lista de contactos

    # Método para mostrar todos los contactos en la agenda
    def mostrar_contactos(self):
        for contacto in self.contactos:  # Itera sobre cada contacto en la lista de contactos
            # Imprime la información del contacto
            print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

# Creando instancias de Contacto
contacto1 = Contacto('Alice', '123456789', 'alice@example.com')
contacto2 = Contacto('Bob', '987654321', 'bob@example.com')

# Creando una instancia de Agenda
mi_agenda = Agenda()

# Agregando contactos a la agenda
mi_agenda.agregar_contacto(contacto1)
mi_agenda.agregar_contacto(contacto2)

# Mostrando todos los contactos en la agenda
mi_agenda.mostrar_contactos()