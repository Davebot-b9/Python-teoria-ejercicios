#Principio de segregacion de la interfaz
#eliminar las dependencias que no se van a usar
from abc import ABC, abstractmethod

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

class Comer(ABC):
    @abstractmethod
    def comer(self):
        pass

class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

class Humano(Trabajador, Durmiente, Comer):
    def comer(self):
        print("El humano esta comiendo")
    
    def trabajar(self):
        print("El humano esta trabajando")
    
    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):
    def trabajar(self):
        print("El Robot esta trabajando")

humano = Humano()
robot = Robot()

humano.comer()
robot.trabajar()