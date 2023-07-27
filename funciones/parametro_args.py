#forma no optima de sumar valores
def suma_lista(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

resultado = suma_lista([5,3,12,34,12])
print(resultado)

#forma optima con el parametro args *
def suma_2(nombre, *numeros): # aqui si ponemos un parametro despues de args, en este caso *numeros lo va a ignorar o omitir, ya que al usar args podemos ingresar infinitos elementos en este caso si quisieramos seria infinita la lista de los numeros
    return f"{nombre}, la suma de tus numeros es: ", sum(numeros)

resultado2 = suma_2("Oscar", 3,35,2,79,3,12)
print(resultado2)


#forma dos de usar args *
def suma_total(numero):
    return sum([*numero]) #acuerdate que es una lista lo que esta retornando: [*numero], sum() realiza la suma

resultado3 = suma_total([1,3,4,5,6,7]) #aqui esta la lista con los valores ingresados

print(resultado3)