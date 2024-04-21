'''
En este contexto, la clase "Persona" es la clase padre,
tiene el método saludar incluido con los atributos nombre y edad
y sus clase hijas son "Profesor" y "Estudiante" que hereda aquellos atributos junto
a definir uno más el cual es el grado del estudiante y la materia del profesor
además de implementar polimorfismo para el método "saludar".
Esto dará un saludo personalizado a cada clase
'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre}."

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia
    def saludar(self):
        mensaje_padre = super().saludar()
        return f"{mensaje_padre} Soy profesor de {self.materia}."
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def saludar(self):
        mensaje_padre = super().saludar()
        return f"{mensaje_padre} Soy estudiante de {self.grado} grado."

# Crear una instancia de Profesor
profesor1 = Profesor("Pedro",25,"Matemáticas")

# Crear una instancia de Estudiante
estudiante1 = Estudiante("Juan", 15, "noveno")

# Llamar el método saludar() de profesor
print(profesor1.saludar())

# Llamar al método saludar() de Estudiante
print(estudiante1.saludar())
