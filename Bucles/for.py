#listas, tuplas, diccionarios, cadenas de texto, conjuntos son iterables

#crenado un ciclo for in
animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [10, 56, 19, 20]

#recorriendo la lista animales
for animal in animales:
    print(animal)
    

#recorriendo la lista numero y multiplicando cada valor por 2
for numero in numeros:
    resultado = numero * 2
    print(resultado)
    

#al recorrer dos listas al mismo tiempo, estas deben de cumplir con: tener el mismo numero de elementos en sus listas, en este caso numeros y animales tienes 4 elementos
for numero,animal in zip(animales, numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")
    

# range() lo que imprime es recorrer los numeros entre el rango que le indiquemos omitiendo el 10 y el 20
# si por ejemplo solo ponemos un numero range(5) recorrera del 0 al 4 unicamente
for num in range(10,20):
    print(num)
    
#forma no optima de recorrer una lista con su indice
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El índice es: {indice} y el valor es: {valor}")

#usando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actial: {numero}')
else:
    print("el bucle termino")

#todo lo anterior se usa igual para las tuplas, conjuntos listas como es el caso sin embargo no es lo mismo para los diccionarios