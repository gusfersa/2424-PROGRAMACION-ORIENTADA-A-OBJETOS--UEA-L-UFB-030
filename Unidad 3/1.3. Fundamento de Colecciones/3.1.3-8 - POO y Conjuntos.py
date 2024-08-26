class Tag:
    def __init__(self, nombre):
        self.nombre = nombre


class Articulo:
    def __init__(self, titulo):
        self.titulo = titulo
        self.tags = set()

    def agregar_tag(self, tag):
        self.tags.add(tag)

    def mostrar_tags(self):
        for tag in self.tags:
            print(tag.nombre)


# Ejemplo de uso
articulo = Articulo("Cómo aprender Python")
articulo.agregar_tag(Tag("programación"))
articulo.agregar_tag(Tag("tutorial"))
articulo.agregar_tag(Tag("Python"))
articulo.mostrar_tags()
