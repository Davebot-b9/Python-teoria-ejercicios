#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
name = input("Ingresa tu nombre completo: ")
mayus = name.upper()
minus = name.lower()
first_letter = name.title() #Cada palabra la inicial la convierte en mayuscula y lo demas en minusculas
print(f"Tu nombre en mayusculas: {mayus}")
print(f"Tu nombre en minusculas: {minus}")
print(f"Tu nombre como las iniciales en mayusculas: {first_letter}")
