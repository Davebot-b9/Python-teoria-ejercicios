#Todo esto no es modular y dificil de definir y mantener
# celular1_marca = "samsung"
# celular2_marca = "apple"
# celular3_marca = "huawei"

# celular1_modelo = "S23"
# celular2_modelo = "iPhone 15 pro"
# celular3_modelo = "P20 pro"

# celular1_camaraT = "48MP"
# celular2_camaraT = "40MP"
# celular3_camaraT = "12MP"

# celular1_camaraF = "48MP"
# celular2_camaraF = "40MP"
# celular3_camaraF = "8MP"

# class Celular(): #aqui declaramos y definimos la clase
    #las variables son atributos de una clase
#     marca = "Samsung"
#     modelo = "S23"
#     camara = "48MP"

# celular1 = Celular() # aqui creamos el objeto, que se llama celular1, un objeto es la instancia de una clase

class Celular:
    # metodo constructor
    def __init__(self, marca, modelo, camara): #self es una referencia de si mismo
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
#el metodo constructor siempre se va a llamar cada que instanciemos la clase en un objeto
celular_1 = Celular("Samsung", "S23","48MP") #aqui declaramos atributos de instancia
celular_2 = Celular("Apple", "iPhone 15","108MP")