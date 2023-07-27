multiplicar_por_dos = lambda x : x*2 #una forma de crear una funcion anonima es usando lambda puede ser una manera sencilla de declarar funciones, retorna automaticamente

#forma comun de declarar una funcion: 

# def multiplicar_dos_num (x):
#     return x*2

print(multiplicar_por_dos(3))

#usando filter con una funcion común
numeros =[1,2,3,4,5,6,7,8]

#creando una funcion que diga si es par o no
# def es_par(num):
#     if(num%2==0):
#         return True

# numeros_pares = filter(es_par, numeros)
#print(list(numeros_pares))

#usando lambda
numeros_pares = filter(lambda numero:numero%2==0, numeros) #aqui en ves de declarar la funcion 'es_par' usamos lambda para realizar la condicion de tru o false si es par o no
print(list(numeros_pares))