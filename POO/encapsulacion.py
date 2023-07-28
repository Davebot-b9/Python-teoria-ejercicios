class Personaje:    
    #Metodo constructor
    def __init__(self, __nombre, __fuerza,__inteligencia,__defensa,__vida): #self es un argumento que hace referencia a si mismo, al objeto para poder dar acceso a los atributos y metodos
        self.__nombre = __nombre
        self.__fuerza = __fuerza
        self.__inteligencia = __inteligencia
        self.__defensa = __defensa
        self.__vida = __vida
    
    def atributos(self):
        print(self.__nombre, ":", sep="")
        print(".fuerza:", self.__fuerza)
        print(".inteligencia:", self.__inteligencia)
        print(".defensa:", self.__defensa)
        print(".vida:", self.__vida)
    
    def subir_nivel(self, __fuerza,__inteligencia,__defensa):
        self.__fuerza = self.__fuerza + __fuerza
        self.__inteligencia = self.__inteligencia + __inteligencia
        self.__defensa = self.__defensa + __defensa
        
    def esta_vivo(self):
        return self.__vida > 0
    
    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")
    
    def daño(self, enemigo):
        return self.__fuerza - enemigo.__defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        if enemigo.esta_vivo():
            print("La __vida de", enemigo.__nombre, "es", enemigo.__vida)
        else:
            enemigo.__morir()

    #metodo get devolvera el atributo
    def get_fuerza(self):
        return self.__fuerza

    #metodo set recibira otro nuevo valor para actualizar el actual
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error, has introducido un valor negativo")
        else:
            self.__fuerza = fuerza

#creando un objeto
mi_personaje = Personaje("MethalDave", 10, 1, 5, 100)
mi_enemigo = Personaje("Enemy ground", 8, 5, 3, 5)

#los metodos al ser funciones dentro de la clase si tienen acceso a los atributos
mi_personaje.atributos()
mi_personaje.atacar(mi_enemigo)

#¿Como modificamos o accedemos a los atributos de la clase Personaje?
#Pues usamos los metodos getter y setter

mi_personaje.set_fuerza(5)
mi_personaje.atributos()