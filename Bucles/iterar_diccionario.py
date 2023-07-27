diccionario = {
    "nombre" : "Oscar",
    "apellido" : "Morelos",
    "edad" : 23
}

#recorriendo diccionario para obtener las claves
for key in diccionario:
    print(key)

#recorriendo un diccionario con items para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")