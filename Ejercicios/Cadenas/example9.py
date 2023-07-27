#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
fecha_nacimiento = input("Introduce tu fecha de nacimiento en el formato dd/mm/aaaa: ")
print(f'Día: {fecha_nacimiento[:2]}')
print(f'Mes: {fecha_nacimiento[3:5]}')
print(f'Año: {fecha_nacimiento[6:10]}')

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Dia: ',dia)
print('Mes: ',mes)
print('Año: ', año)