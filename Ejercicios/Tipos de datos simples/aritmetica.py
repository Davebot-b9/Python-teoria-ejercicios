#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética (3+2/2*5)**2

print(((3 + 2) / (2 * 5))**2)

#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los primeros n enteros positivos puede ser calculada de la siguiente forma:
#  Suma = (n(n+1))/2

n = int(input("Introduce un numero: "))
suma = n * (n + 1) / 2
print("La suma de los primeros numeros enteros desde 1 hasta " + str(n) + " es " + str(suma))

# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n = int(input("Ingresa un numero entero: "))
m = int(input("Ingresa otro numero entero: "))
c = n // m
r = n % m
print("El cociente de la division de los dos numeros es: " + str(c) + " y el residuo de la divison de los dos numeros enteros es: " + str(r))
