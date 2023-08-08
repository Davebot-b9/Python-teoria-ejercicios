from abc import ABC, abstractclassmethod
#las clases abstractas se usan para crear plantillas para tomar como punto de partida, ademas que en el tema de seguridad beneficia y aun más cuando la convinas con encapsulamiento, cabe resaltar que los metodos que creemos en nuestra plantilla, osea la clase abstracta nos obliga a forzosamente usar los metodos que declaremos
class Perona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, actividad, sexo):
        #super().__init__()
        self.nombre = nombre
        self.edad = edad
        self.actividad = actividad
        self.sexo = sexo
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Me llamo: {self.nombre} y tengo {self.edad} años")

#clase 1 que hereda de plantilla Persona()
class Estudiante(Perona):
    def __init__(self, nombre,edad,actividad,sexo):
        super().__init__(nombre, edad, actividad, sexo)
    
    def hacer_actividad(self):
        print("Estoy estudiando:", self.actividad)

#clase 2 que hereda de plantilla Persona()
class Trabajador(Perona):
    def __init__(self, nombre,edad,actividad,sexo):
        super().__init__(nombre, edad, actividad, sexo)
    
    def hacer_actividad(self):
        print("Actualmente estoy trabajando en el rubro de:", self.actividad)

oscar = Estudiante("Oscar", 23, "Programacion", "Masculino")

david = Trabajador("David",25,"Programacion", "Masculino")

oscar.presentarse()
oscar.hacer_actividad()

david.presentarse()
david.hacer_actividad()