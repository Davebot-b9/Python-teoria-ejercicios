#creando diccionario con dic()

diccionario = dict(nombre="osacr", apellido="morelos")

#las listas no pueden ser llaves, osea no pueden ser iterables
diccionario1 = {frozenset(["oscar", "david"]): "jajaja"}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])

#creando diccionarios con fromkeys() con dos parametros
#en fromkeys el primer valor es iterable
diccionario = dict.fromkeys(["nombre", "apellido"], "No se")


#print(diccionario2["nombre"])
print(diccionario)