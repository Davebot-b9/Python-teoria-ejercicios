#creando una funcion simple
def saludar():
    print("hola como estas, esta es mi primer funcion simple")
#ejecutando la funcion simple
saludar()

#crear una funcion que tenga parametros
#parametros son variables que se usan dentro de la funcion
def saludar_otro(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "cielo"
    else:
        adjetivo = 'amor'
    print(f"Hola {nombre}, mi {adjetivo} ¿Cómo estas?")
    
saludar_otro("Camila", "Mujer") #ingresamos como parametros string
saludar_otro("Oscar", "HoMBre")
saludar_otro("Fran", "No binario")

#crear una funcion que nos retorne valores
def crear_contraseña_random(num): #ejemplo si num es 5
    chars = "asdleuadeff"
    num_entero = str(num) #convertimos el primer numero a string
    num = int(num_entero[0]) #convertimos el primer numero a entero y obtenemos el primer caracter
    c1 = num - 2 #num = 5 por lo que num es 3
    c2 = num # num = 5
    c3 = num - 5 # num = 5 entonces es 0
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}" #cadena de la contraseña
    return contraseña, num

#crear_contraseña_random(23) # en este caso si genera la contraseña pero no la muestra en pantalla

#para mostrar en pantalla lo que genero la funcion sería lo siguiente:
# password = crear_contraseña_random(3)
# frase = f"Tu contraseña nueva es: {password}"
# print(frase)

#desempaquetar
password,primer_numero = crear_contraseña_random(398) #apesar de ser un numero grande solo toma en cuenta el primer digito

print(f"Tu contraseña nueva es: {password}")
print(f"El numero utilizado para crearla fue: {primer_numero}")