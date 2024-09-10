import json

class Libro:
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.prestado = prestado

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado
        }

class Biblioteca:
    def __init__(self, archivo_json='biblioteca.json'):
        self.archivo_json = archivo_json
        self.libros = self.cargar_libros()

    def cargar_libros(self):
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos_libros = json.load(archivo)
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except FileNotFoundError:
            return {}

    def guardar_libros(self):
        with open(self.archivo_json, 'w') as archivo:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar_libros()

    def prestar_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro and not libro.prestado:
            libro.prestado = True
            self.guardar_libros()
            print(f"Libro {isbn} prestado con éxito.")
        else:
            print("Libro no disponible para préstamo.")

    def devolver_libro(self, isbn):
        libro = self.libros.get(isbn)
        if libro and libro.prestado:
            libro.prestado = False
            self.guardar_libros()
            print(f"Libro {isbn} devuelto con éxito.")
        else:
            print("Error en la devolución del libro.")

    def mostrar_libros(self):
        for libro in self.libros.values():
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Añadir Libro\n2. Mostrar Libros\n3. Prestar Libro\n4. Devolver Libro\n5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)
        elif opcion == '2':
            biblioteca.mostrar_libros()
        elif opcion == '3':
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(isbn)
        elif opcion == '4':
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(isbn)
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
