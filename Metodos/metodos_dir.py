diccionario = {
    "nombre" : "oscar",
    "apellido" : "morelos",
    "edad" : 23
}

#devuelve las claves: nombre, apellido, edad (sirve tambien para iterar)
claves = diccionario.keys()

#metodo get obtiene un elemento (sino encuentra nada el programa continua)
claves = diccionario.get("apellido")

#eliminando todo el diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("nombre")

#devuelve el diccionario, podemos iterar recorrer los elementos del diccionario
diccionario_iterable = diccionario.items()

print(claves)