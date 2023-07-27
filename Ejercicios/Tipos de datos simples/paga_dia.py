#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
horas = float(input("¿Cuantas horas laboraste hoy?: "))
coste = float(input("¿Cuanto cobras por hora?: "))
pago_final = horas * coste

print("Tu paga por hoy es de: ", pago_final)
