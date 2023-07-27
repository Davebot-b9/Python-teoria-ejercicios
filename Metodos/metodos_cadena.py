cadena1 = "5520298333"
cadena2 = "Buen día, hay mucho, por hacer, y no, podemos, perder el tiempo"
cadena3 = "Hola soy Oscar"
cadena4 = "Fasheu"

#estructura de un metodo o llamar a un metodo es:
# DATO . METODO(Parametros)

mayus = cadena2.upper() # upper convierte la cadena de texto a mayusculas
minus = cadena3.lower() # convierte a minusculas
primer_letra_mayus = cadena1.capitalize() #convierte la primer letra de la cadena en mayúscula

#buscamos una cadena en otra cadena, si no hay coincidencia nos devuelve -1
busqueda_find = cadena2.find("a")

busqueda_index = cadena3.index("o") # si no hay coincidencias nos lanza una excepcion
print(busqueda_index)

#si es numerico, devolvemos true, sino es numerico devuelve false
es_numerico = cadena1.isnumeric()

print(es_numerico)

#si es alfanumerico, devolvemos true, sino es alfanumerico devuelve false

es_alfanumerico = cadena4.isalpha() # solo es valido de la A - Z, no son validos los espacios, por lo que no acepta caracteres especiales, si se cumple nos va a devolver True
print(es_alfanumerico)

#buscamos una cadena en otra cadena, devuelve la cantidad de veces  que coincida
#sino encuentra coincidencias devuelve 0
contar_coincidencias = cadena2.count("a")
print(contar_coincidencias) #print es una funcion, no un metodo

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena3) # len es una funcion, no un metodo
print(contar_caracteres)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena2.startswith("B")
print(empieza_con)
#verificamos si una cadena termina con otra cadena dada, si es asi devulver true
termina_en = cadena2.endswith("r")

#Reemplaza un pedazo de una cadena dada por otra, si el valor 1 se encuentra en la cadena original, remplaza el valor 1 de la misma por el valor 2 osea el nuevo valor

cadena_nueva = cadena3.replace("Oscar","la cadena nueva")
print(cadena_nueva)

# separar cadenas con la cadena que le pasemos
cadena_separada = cadena2.split(",")
print(cadena_separada)
print(type(cadena_separada)) # split separa todo por lo que le pasemos, en este caso fue una coma "," y crea una lista

# Ejemplo de como invertir cadenas
frase = input("Introduce una frase: ")
print(frase[::-1]) # invierte la frase