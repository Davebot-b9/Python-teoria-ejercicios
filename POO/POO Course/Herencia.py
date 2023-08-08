class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print("Hola estoy hablando contigo")
#clase 1 hereda de persona
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
#clase 2 hereda de persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, calificaciones, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.calificaciones = calificaciones
        self.universidad = universidad
#una herencia gerarquica es aquella que una clase padre le hereda todas sus propiedades y metodos a dos o más clases

roberto = Empleado("Roberto", 23, "Mexicana", "Programador", 10000)

print(roberto.nombre)
roberto.hablar()