#creando una funcion de 3 parametros keywords parameters
#def frase(nombre, apellido,adjetivo):
#    return f'hola {nombre} {apellido}, eres muy {adjetivo}'

#frase_resultante = frase("Oscar","Morelos", "listo")
# frase_resultante = frase(adjetivo = "listo",nombre = "Oscar", apellido = "Morelos") no se altera el orden, como se declara el orden de los parametros es como se imprimen

#la misma funcion con un parametro opcional y un valor por defecto en este caso el opcional vendría siendo 'nombre' y 'apellido', y con un valor por defecto es 'adjetivo'
def frase(nombre, apellido,adjetivo = "Tonto"): #aqui se pueden definir por defecto
    return f'hola {nombre} {apellido}, eres muy {adjetivo}'

frase_resultante = frase("Oscar","Morelos")#, adjetivo="inteligente") si deseamos cambiar la definiciob de un parametro es como lo muestro aqui^
print(frase_resultante)