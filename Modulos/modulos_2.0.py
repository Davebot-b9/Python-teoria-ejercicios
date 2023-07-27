#import funciones_buenas.saludar 

#print(funciones_buenas.saludar.Saludar("Oscar"))

# si el modulo estuviera dentro de una carpeta en la misma ruta
# import funciones_buenas.saludar as m_saludar
# print(m_saludar.Saludar("Oscar"))

import sys

sys.path.append("c:\\Users\\novem\\Desktop\\Python Curso\\funciones_buenas")

import saludar as m_saludo

print(m_saludo.Saludar("Oscar"))