#consume menos recursos, por defecto abre el archivo y ejecutamos las instrucciones que queramos, en este caso leer y mostrar en pantalla lo que hay dentro del archivo .txt y al terminar de leer se cierra por defecto
with open("archivos\\mensaje_texto.txt", encoding="UTF-8") as archivo:
    #leemos el archivo
    contenido = archivo.read()
    #mostramos el archivo
    print(contenido)
#se cierra el archivo al usar with open
