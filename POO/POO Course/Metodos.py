class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f"Estas haciendo una llamada desde un {self.modelo}")
    def cortar(self):
        print(f"Has cortado la llamada desde tu: {self.modelo}") #self es para auto referenciarse

celular_1 = Celular("Samsung", "S23","48MP")
celular_2 = Celular("Apple", "iPhone 15","108MP")
celular_1.llamar()
celular_2.cortar()