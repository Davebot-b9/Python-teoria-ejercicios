#creando mi propia excepcion
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"El error es: {err}")
        
#Lanzando mi propia excepcion
#raise MiExcepcion("Jajajaja haz cometido un grave error")

#manejandola
try:
    raise MiExcepcion("Cometiste un error")
except:
    print("Como vas a cometer ese error?")