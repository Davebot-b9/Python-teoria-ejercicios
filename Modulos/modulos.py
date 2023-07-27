#import modulo_saludar as m_saludar #importamos el modulo y 'modulo_saludar' se convierte en la definicion y 'm_saludar' en la variable que se usara para declarar los metodos del modulo donde se definen

#lo almacenamos en una variable y lo mandamos a llamar, le asignamos su parametro
#saludar = m_saludar.saludar("Ana") # esto es un metodo
#imprimimos resultado
#print(saludar)

#otra forma sin necesidad de llamar al modulo y depues la convertimos en funcion, simplemente llamando al metodo saludar y asignandole el parametro
# from modulo_saludar import saludar
# saludo = saludar("David") #esto es una funcion
# print(saludo)

#llamando a dos o mas funciones o metodos
from modulo_saludar import Saludar,Saludar_raro as s_raro # si deseamos importar todo solo es: 'import *' lo que no es recomendable por que el programa se puede volver mas pesado, es una mala practica pero es bueno conocerlo
saludo = Saludar("oscar").upper()
saludo_r = s_raro("dave").lower()
print(saludo)
print(saludo_r)

#para ver las propiedades y metodos de e namespace
#print(dir(m_saludar))

#accedemos al nombre de este modulo
print(__name__)

# accedemos al nombre del modulo  llamado
#print(s_raro.__name__) # para mostrar el nombre real de la funcion