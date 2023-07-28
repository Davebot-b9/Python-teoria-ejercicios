class Personaje:
    #pass #pass es para que hasta el momento no haga nada la clase
    #No es necesario inicializar los atributos al inicio, para ello mejor usa el metodo constructor
    # nombre = "Default"
    # fuerza = 0
    # inteligencia = 0
    # defensa = 0
    # vida = 0
    
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
#creando un objeto
mi_personaje = Personaje("MethalDave", 10, 1, 5, 100)
mi_enemigo = Personaje("Enemy ground", 8, 5, 3, 5)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()
# print(mi_personaje.atacar(mi_enemigo))
# mi_enemigo.atributos()
# mi_personaje.morir()
# mi_personaje.atributos()

#mi_personaje.subir_nivel(1,2,0)
#mi_personaje.atributos() si se desea ver los stats actualizados al subir de nivel se vuelve a llamar al metodo para que se vean reflejada la actualizacion
#print(mi_personaje.esta_vivo())

# mi_personaje.nombre = "MethalDave"
# mi_personaje.fuerza = 10

# print("El nombre del jugador es: ", mi_personaje.nombre)
# print("La fuerza del jugador es: ", mi_personaje.fuerza)