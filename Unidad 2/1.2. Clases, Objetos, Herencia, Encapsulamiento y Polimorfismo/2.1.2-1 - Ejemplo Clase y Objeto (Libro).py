# En este ejemplo, la clase Libro tiene tres atributos: titulo, autor y paginas.
# Además, tiene un método informacion que devuelve una descripción del libro.

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def informacion(self):
        return f"{self.titulo} escrito por {self.autor}, {self.paginas} páginas"


# Instanciación
# Suponiendo que tenemos una clase 'Libro' definida previamente
mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 417)
print(mi_libro.informacion())