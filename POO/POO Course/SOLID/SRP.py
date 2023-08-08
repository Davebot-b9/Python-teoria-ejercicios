#Principio de responsabilidad unica SRP
class TanqueDeCombustible:
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class Auto():
    def __init__(self, tanque):
        self.posicion = 0 #atributo estatico
        self.tanque = tanque # atributo de instancia
    
    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Haz movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")
    
    def obtener_posicion(self):
        return self.posicion

tanque = TanqueDeCombustible()
carrito = Auto(tanque)

print(carrito.obtener_posicion())
carrito.mover(10)
print(carrito.obtener_posicion())
carrito.mover(20)
print(carrito.obtener_posicion())
carrito.mover(30)
print(carrito.obtener_posicion())
carrito.mover(60)
print(carrito.obtener_posicion())
carrito.mover(100)
