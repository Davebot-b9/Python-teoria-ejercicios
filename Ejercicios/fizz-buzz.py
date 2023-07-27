#El Fizz Buzz es un ejercicio clásico utilizado en entrevistas de programación para evaluar las habilidades básicas de programación de un candidato. Es un problema simple pero puede revelar mucho sobre el pensamiento lógico y la capacidad de escribir código de manera clara y concisa.

#La regla básica de Fizz Buzz es la siguiente:

#Se le pide al candidato que escriba un programa que imprima los números del 1 al N, donde N es un número dado.
#Si el número es divisible por 3, en lugar del número, el programa debe imprimir "Fizz".
#Si el número es divisible por 5, en lugar del número, el programa debe imprimir "Buzz".
#Si el número es divisible tanto por 3 como por 5, el programa debe imprimir "FizzBuzz".

# Por ejemplo, si N = 15, la salida debería ser:

# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

# El propósito de esta prueba es evaluar la capacidad del candidato para utilizar estructuras de control como bucles y condicionales, y también para verificar si comprenden conceptos básicos como operaciones aritméticas y módulo (para verificar divisibilidad).

def fizz_buzz(n):
    for i in range(1, n + 1):
        #is the number a multiple of 3 and 5?
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=", ")
        # is the number a multiple of 3
        elif i % 3 == 0:
            print("Fizz", end=", ")
        # is the number a multiple of 5
        elif i % 5 == 0:
            print("Buzz", end=", ")
        else:
            print(i, end=", ")
#hasta 100
fizz_buzz(100)
print("\n-------------------")

# Otra forma de resolver esto es sin usar el operador de % modulo
def is_divisible (num, divisor):
    return num - (num // divisor) * divisor == 0

def fizz_buzz_2(n):
    for i in range(1, n + 1):
        fizz = is_divisible(i, 3)
        buzz = is_divisible(i, 5)

        if fizz and buzz:
            print("FizzBuzz", end=", ")
        elif fizz:
            print("Fizz", end=", ")
        elif buzz:
            print("Buzz", end=", ")
        else:
            print(i, end=", ")
fizz_buzz_2(15)