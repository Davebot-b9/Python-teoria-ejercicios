#creando una funcion que nos devuelva los numeros primos
#entre 0 y el argumento que pasamos

#crear una funcion que verifique si un numero es primo
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse por nungun numero entre 2 y ese mismo numero - 1
    for i in range(2, num - 1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num % i == 0: return False
        #si termine el bucle, significa que no fue divisible entonces es primo
    return True

#creando funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #creamos la lista
    primos = []
    for i in range(3,num+1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #en caso de que lo sea lo agregamos a la lista
        if resultado == True: primos.append(i)
    return primos

resultado2 = primos_hasta(13)
print(resultado2)

#forma mas sencilla de mostrar primos
primos_num_hasta = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), range(2, num)))

print(primos_num_hasta(15))
