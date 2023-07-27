import re

text = """Hola. Esto es una cadena 212. larga para poder usar expresiones regulares
es necesario aprender esta herramienta 357 de python para poder_entender_temas un poco más avanzados 4.
Esta es una linea de texto final 11. Final"""

#haciendo una busqueda simple
#resultado = re.search("Hola", text)
#resultado2 = re.findall("es", text, flags=re.IGNORECASE) #buscar todas las coincidencias e ignorar las que tengan mayusculas
#print(resultado)
#print(resultado2)

#\d -> busca digitos numericos del 0 - 9
#resultado = re.findall(r"\d", text)

#\D -> busca TODO menos digitos numericos del 0 - 9
#resultado = re.findall(r"\D", text)


#\w -> busca caracteres alfanumericos[a-z A-Z 0-9 _]
#resultado = re.findall(r"\w", text)

#\W -> busca TODO menos caracteres alfanumericos[a-z A-Z 0-9 _]
# resultado = re.findall(r"\W", text)


#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea
#resultado = re.findall(r"\s", text)

#\S -> busca TODO menos espacios en blanco -> espacios, tabs, saltos de linea
# resultado = re.findall(r"\S", text)


#. -> busca TODO menos saltos en linea
# resultado = re.findall(r".", text)


#\n -> busca saltos en linea
# resultado = re.findall(r'\n',text)


#\ -> cancelar caracteres especiales
# resultado = re.findall(r'\.',text)


#armando una cadena que busque un numero, seguido de un punto y un espacio
# resultado = re.findall(r'\d\.\s', text)


#buscando el principio de una linea
#^ -> busca el comienzo de una linea
#flags = re.M activa la multilinea
#resultado = re.findall(f'^Esta',text, flags=re.M)

#buscando el final de una linea
#^ -> busca el final de una linea
#resultado = re.findall(f'Final$',text, flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda
#resultado = re.findall(r'\d{3}\s', text)


#{n,m} -> al menos n, como maximo m
#resultado = re.findall(r'\d{1,4}', text)

# | busca una cosa o la otra
resultado = re.findall(r'\d{1,4}|Hola',text)
print(resultado)