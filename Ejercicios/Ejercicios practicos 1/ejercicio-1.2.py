frase = input("Dime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

if cantidad_de_palabras > 120:
    print("Espera tampoco es una biblia")

print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo")

print(f"Otra persona lo diria en {round(cantidad_de_palabras/2*1.3, 1)} segundos")