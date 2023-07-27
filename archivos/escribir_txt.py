#para poder escribir en el archivo agregamos 'w' como segundo parametro para indicar que escribiremos en el archivo
with open("archivos\\mensaje_texto.txt", 'w', encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("jajajaja ya escribi aqui!!")
    
    #sobreescribimos mas de una linea
    archivo.writelines(["Hola amigo como estas\n", "otra linea jajaja\n"])
    #agregando otras dos lineas
    archivo.writelines(["bien tu como Andas\n", "otra linea de nuevo jajaja"])