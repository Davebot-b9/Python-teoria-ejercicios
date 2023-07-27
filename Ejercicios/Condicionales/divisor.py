#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

while True:
    dividendo = float(input("Introduce el dividendo: "))
    divisor = float(input("Introduce el divisor: "))

    if divisor == 0:
        print("Error el divisor es un 0, intentalo de nuevo")
    else:
        print(dividendo/divisor)
        break