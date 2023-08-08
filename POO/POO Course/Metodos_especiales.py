class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f'Persona(nombre = {self.nombre}, edad ={self.edad})'
    
    def __repr__(self) -> str:
        return f'Persona("{self.nombre}",{self.edad})'
    
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)

oscar = Persona("Oscar", 23)
david = Persona("David", 25)

nueva_persona = oscar + david
print(nueva_persona.nombre)
# repre = repr(oscar)
# resultado = eval(repre)
# print(resultado.edad)