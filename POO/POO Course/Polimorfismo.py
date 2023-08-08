class Animal(): #aqui podríamos usar polimorfismo de herencia 
    def sonido(self):
        pass
    # def sonido(self, nombre): aqui usamos polimorfismo de sobrecarga, cada uno se llama igual pero se comporta distinto, por que? pues esto es por que cada metodo tiene distintos numero de parametros, eso es lo que los diferencia entre si, pero en python no es posible usar almenos como se declara aqui polimorfismo de sobrecarga
    #     pass
    # def sonido(self, nombre, edad):
    #     pass

class Gato(Animal):
    def sonido(self):
        return "Miau"

class Perro(Animal):
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())
#el polimorfismo en este caso se usa para llamar a un metodo que tiene el mismo nombre sin embargo se comporta cada una de una forma distinta, esto no se limita a solo los metodos, puede haber polimorfismo de variables
gato = Gato()
perro = Perro()

print(perro.sonido()) #una forma de polimorfismo
hacer_sonido(gato) #otra forma de polimorfismo usando la funcion 'hacer_sonido(animal)'

#duck typing enlaces dinamicos y estaticos
#tipo real y declarado