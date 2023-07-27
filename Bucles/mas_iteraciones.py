#creando las listas
frutas = ["platano", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]

#evitando que se coma una granada con la sentencia continue
for fruta in frutas:
    if fruta == 'granada':
        continue # cuando fruta vale en este caso "granada" lo que hace continue, es saltar ese valor y continua el bucle, simplemente omite mostrar en pantalla dada la conicion que le indiquemos
    print(f"Me voy a comer una {fruta}")

#evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == 'pera':
        break #rompe con el bucle y con todo lo demás, por ejemplo si pongo un else lo va a omitir, sin embargo si pongo un print() si va a imprimir en pantalla
else:
    print("terminado")

#recorrer una cadena de texto
cadena = "Hola como estas"
for letra in cadena:
    print(letra)

numeros = [2,4,5,7]
#for en una sola linea
numeros_duplicados = [x * 2 for x in numeros]
print(numeros_duplicados)