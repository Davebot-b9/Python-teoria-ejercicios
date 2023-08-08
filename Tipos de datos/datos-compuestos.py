#Lista es un tipo de dato compuesto, parecido a una matriz, una lista puede ser modificable
#         indice 0     indice 1     indice 2 ...
lista = ["Oscar Dav", "Itzana studios", True, 1999, 1.60]

print(lista[1])

# Tuplas, no se puede modificar la tupla

tupla = ("Oscar Dav", "Itzana studios", True, 1999, 1.60)
#print(tupla[3])

#Conjunto (set), puede intercambiar elementos de lugar pero no puede alterarlos, sin embargo si se puede redefinir un conjunto(set)

conjunto = {"Hola", "set", 234, 2.3}

#esto no se puede
#conjunto[2] = "No se puede"

#esto si se puede
conjunto = {"Puede redefinirse"}

#no puede mostrar en consola el valor de algun índice, para poder acceder a algun indice es necesario utilizar un bucle
#print(conjunto[3])

#en un conjunto si hay algun indice duplicado, este no va a ser mostrado en pantalla
conjunto = {"Hola", "set", 234, 2.3, 234}

#diciionario
#no tiene un orden, la estructura de un diccionario es 'key' o clave : 'value' o valor y separamos con comas
diccionario = {
    #key     :   value
    'nombre' : 'Oscar David',
    'profesion' : 'Músico',
    'edad' : 23,
    'esta cansado' : True,
    'altura' : 1.60,
    'dato duplicado' : 'Músico'
}
#                   key
print(diccionario['nombre'])