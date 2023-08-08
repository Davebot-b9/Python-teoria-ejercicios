# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

año = int(input("Cual es tu edad? "))

for i in range(año):
    print(f"Haz cumplido {i+1} años")