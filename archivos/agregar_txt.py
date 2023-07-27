with open("archivos\\mensaje_texto.txt", 'a', encoding="UTF-8") as archivo:
    #agregando el archivo
    archivo.write("\njajajaa ahora voy a agregar varias lineas, sin sobreescribir la informacion del archivo\n")
    #usando un bucle para agregar varias lineas
    for i in range(5):
        archivo.write(f"Linea {i+1} agregada\n")