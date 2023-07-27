def sumas_dos():
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #si se cumple el try directamente se pasa al else, ejecuta el break y termina el bucle while
        try:
            resultado = int(a) + int(b)
        except Exception as e:
            #en caso de ingresar un caracter lanza el siguiente mensaje por lo que se repite el ingresas dos numeros
            print("Te pedi un numero, no es valido lo que ingresaste")
            print(f"Eror: {type(e).__name__}")
        else:
            break
        #el finally siempre se va a ejecutar
        finally:
            print("esto se ejecuta siempre")
    #retorna el resultado una vez que se hayan ingresado los datos correctamente
    return resultado

print(sumas_dos())