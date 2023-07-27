#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
while True: 
    password = input("Introduce una contraseña: ")
    verificar = input("Introduce nuevamente la contraseña que ingresaste: ")
    if password == verificar:
        print("La contraseña es correcta")
        break
    else:
        print("La contraseña no es la misma que ingresaste, vuelve a intentarlo")