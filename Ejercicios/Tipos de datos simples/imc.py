# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = input("Ingresa tu peso en kg: ")
estatura = input("Ingresa tu estatura en metros: ")

imc = round(float(peso) / float(estatura)**2,2) #round redondea un tipo float se realiza la operacion y despues de la "," indicar los subindices o decimales que deseamos mostrar

print("Tu índice de masa corporal es: " + str(imc))