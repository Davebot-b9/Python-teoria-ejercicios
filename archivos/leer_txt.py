#archivo sin leer
archivo_sin_leer = open("archivos\\mensaje_texto.txt", encoding="UTF-8")

#leemos el archivo
#archivo = archivo_sin_leer.read() #una ves que abrimos el archivo y lo leemos, debe cerrarse o comentar el codigo en este caso es por el proceso 'read' que se ha utilizado una vez, esto es por seguridad

#leer linea por linea
#lineas = archivo_sin_leer.readlines()

#leer una sola linea
linea = archivo_sin_leer.readline()

#cerrar el archivo, sirve para no perder datos, para que una vez que se haya consultado su contenido debe cerrarse, si se desea volver a acceder a la informacion es necesario volver a abrirlo con 'open()'
archivo_sin_leer.close()

print(linea)
