class Estudiante:
    def __init__(self, nombre, id_estudiante):
        self.nombre = nombre
        self.id_estudiante = id_estudiante


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante.nombre, estudiante.id_estudiante)


# Ejemplo de uso
curso_python = Curso("Programación en Python")
curso_python.agregar_estudiante(Estudiante("Ana", 1))
curso_python.agregar_estudiante(Estudiante("Luis", 2))
curso_python.mostrar_estudiantes()
