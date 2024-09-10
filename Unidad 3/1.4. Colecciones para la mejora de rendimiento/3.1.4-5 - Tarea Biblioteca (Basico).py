class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        # Tupla para atributos inmutables
        self.info = (isbn, titulo, autor)
        self.categoria = categoria

    def __str__(self):
        return f"ISBN: {self.info[0]}, Título: {self.info[1]}, Autor: {self.info[2]}, Categoría: {self.categoria}"

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        # Lista para gestionar libros prestados
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.info[0] == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        return f"Usuario: {self.id_usuario}, Nombre: {self.nombre}, Libros Prestados: {[libro.info[1] for libro in self.libros_prestados]}"

class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar libros
        self.libros = {}
        # Conjunto para IDs de usuario únicos
        self.usuarios = set()

    def añadir_libro(self, libro):
        self.libros[libro.info[0]] = libro

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            # Simulación de la lógica de préstamo
            print(f"Libro {isbn} prestado al usuario {id_usuario}.")

    def mostrar_libros(self):
        for isbn, libro in self.libros.items():
            print(libro)

# Ejemplo de uso
libro1 = Libro("123-456-789", "Python Avanzado", "Juan Pérez", "Programación")
usuario1 = Usuario("U001", "Ana Gómez")
biblioteca = Biblioteca()
biblioteca.añadir_libro(libro1)
biblioteca.registrar_usuario(usuario1)

usuario1.prestar_libro(libro1)
print(usuario1)
biblioteca.prestar_libro("U001", "123-456-789")
biblioteca.mostrar_libros()
