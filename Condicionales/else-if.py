ingreso_mensual = 5000
gasto_mensual = 8000

#elif anidados
if ingreso_mensual > 100000:
    print("estas bien economicamente en cualquier parte del mundo")
elif ingreso_mensual > 1000: #elif es else if en python
    print("estas bien economicamente en latinoamerica")
else:
    print("por pobre")

if ingreso_mensual > 10000:
    if gasto_mensual - gasto_mensual < 0:#if anidados solo en caso de querer que se cumplan dos condiciones al mismo tiempo
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Ahora si estas bien")
    else:
        print("estas gastando de más")