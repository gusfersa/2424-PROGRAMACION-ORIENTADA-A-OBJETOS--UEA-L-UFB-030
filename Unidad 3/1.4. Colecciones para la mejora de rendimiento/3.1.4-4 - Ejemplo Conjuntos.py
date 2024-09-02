class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = set()  # Conjunto para almacenar estudiantes únicos

    def inscribir_estudiante(self, estudiante):
        if estudiante not in self.estudiantes:
            self.estudiantes.add(estudiante)
            print(f"Estudiante {estudiante} inscrito con éxito en {self.nombre}.")
        else:
            print(f"Estudiante {estudiante} ya está inscrito en {self.nombre}.")

curso_python = Curso("Programación en Python")
curso_python.inscribir_estudiante("Juan Pérez")
curso_python.inscribir_estudiante("Ana Gómez")
curso_python.inscribir_estudiante("Juan Pérez")  # Intento de duplicar inscripción
