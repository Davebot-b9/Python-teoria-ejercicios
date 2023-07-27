#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
invertir_cantidad = float(input("Cantidad que desea invertir: "))
interes_anual = float(input("Interes porcentual anual: "))
años = int(input("Ingrese cuantos años: "))

print("Capital final: " + str(round(invertir_cantidad * (interes_anual/100+1)**años, 2)))