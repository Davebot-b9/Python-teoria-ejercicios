#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
num = int(input("Introduce un numero entero: "))

if num % 2 == 0:
    print(f'El numero {num} es par')
else:
    print(f'El numero {num} es impar')