numeros = [2,3,7,45,18]

# encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#enconntrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando a 6 decimales
numero = round(12.3457834574, 2)

#retorna false -> 0, vacio, False, ninguno
resultado_bool = bool()# 0, vacio, False, None como parametro
resultado_bool_2 = bool("hola nos va a salir true")
print(resultado_bool)

#retorna True, si todo los valores son verdaderos
resultado_all = all([123, "True", [246, 796]])
print(resultado_bool_2)

#suma todos lo valores de un iterable
suma_total = sum(numeros)
print(suma_total)