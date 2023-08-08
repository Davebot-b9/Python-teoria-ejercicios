class Persona:
    def __init__(self, nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property #property lo que hace es convertir un metodo en una propiedad por lo que al llamar al metodo no es necesario terminar con parentesis
    def nombre(self):
        return self.__nombre
    
    @nombre.setter #para poder usar setter en decoradores es @nombre_del_metodo_getter.setter y listo para poder modificarse
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    # @nombre.deleter elimina propiedades
    # def nombre(self):
    #     del self.__nombre

oscar = Persona("Oscar",23)

nombre = oscar.nombre
print(nombre)

oscar.nombre = "David"
nombre = oscar.nombre
print(nombre)

