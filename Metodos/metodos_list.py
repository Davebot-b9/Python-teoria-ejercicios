#Creando una lista con list()
lista = list(["hola", "oscar", 345, 2903, 12, True])

#devuelve la cantidad de elementos de la lista
resultado = len(lista)

#agregando un elemento a la lista
lista.append("aaaaahhhhh")

#agregando un elemento a la lista en un indice especifico
lista.insert(2, "Un nuevo agregado")

#agregar varios elementos a la lista
lista.extend([False, 2712])

#eliminando un elemento de la lista por su indice
lista.pop(0)

#truco para eliminar el ultimo elemento de la lista
#lista.pop(-1) puedes usar -2 para eliminar el penultimo elemento

#removiendo un elemento de la lista por su valor
lista.remove(345)

#eliminando todos los elementos de la lista
#lista.clear()

#en una lista para usar sort no se permiten cadenas de texto
#lista2 = list([234, 12, 0938, 2738, True])
#si se agregegan valores booleanos a la lista, por defecto se ordenan primero los false y despues los true, de ahi numeros
#lista2.sort() #lista2.sort(reverse=True) ordena en reversa los elementos de la lista de manera desendente

#invirtiendo los elemento de una lista
#lista2.reverse() #no ordena la lista

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(12)

print(elemento_encontrado)