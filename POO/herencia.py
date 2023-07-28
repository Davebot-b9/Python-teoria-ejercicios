class Personaje:
    #Metodo constructor
    def __init__(self, nombre, fuerza,inteligencia,defensa,vida): #self es un argumento que hace referencia a si mismo, al objeto para poder dar acceso a los atributos y metodos
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre, ":", sep="")
        print(".Fuerza:", self.fuerza)
        print(".Inteligencia:", self.inteligencia)
        print(".Defensa:", self.defensa)
        print(".Vida:", self.vida)
    
    def subir_nivel(self, fuerza,inteligencia,defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
    
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

class Guerrero(Personaje): #Aqui se aplica la herencia, primero se cre la clase en este caso llamada Guerrero y entre los parentesis indicamos de que clase queremos que herede, asi que llamamos a Personaje para heredar los metodos y atributos de esta Clase Padre
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daños 8. (2) Matadragones, daño 10 "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Numero de arma incorrecto")

    def atributos(self):
        super().atributos()
        print(".Espada:", self.espada)

    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa

# warrior = Guerrero("Midas", 11,2,6,100,5)
# warrior.cambiar_arma()
# warrior.atributos()
#print(warrior.nombre) comprobamos si podemos acceder a los atributos

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    def atributos(self):
        super().atributos()
        print(".Libro: ", self.libro)
    
    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

kratos = Personaje("Kratos", 20, 10, 8, 100)
warrior = Guerrero("Alin", 25, 8, 10, 100, 5)
zatana = Mago("Zatana", 10, 15, 6, 100, 5)

#atacando
kratos.atacar(warrior)
warrior.atacar(zatana)
zatana.atacar(kratos)

#stats despues del daño recibido
kratos.atributos()
warrior.atributos()
zatana.atributos()