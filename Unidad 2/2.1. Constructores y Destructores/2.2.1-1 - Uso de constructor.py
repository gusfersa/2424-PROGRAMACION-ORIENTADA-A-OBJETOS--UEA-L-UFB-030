# Ejemplo de Creación de Objetos:
# "Consideremos una clase Libro con un constructor definido.
# La creación de un objeto Libro se vería así en Python:"

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez")

# "Aquí, mi_libro es una instancia de la clase Libro, y se le pasan 'Cien Años de Soledad'
# y 'Gabriel García Márquez' como argumentos al constructor."