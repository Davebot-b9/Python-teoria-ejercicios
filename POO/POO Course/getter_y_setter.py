class Persona:
    def __init__(self, nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self): #el metodo get nos permite acceder a la definicion de la varable privada
        return self.__nombre
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre

oscar = Persona("Oscar",23)

nombre = oscar.get_nombre()
print(nombre)

oscar.set_nombre('David')

nombre = oscar.get_nombre()
print(nombre)