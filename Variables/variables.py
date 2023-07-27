# declaracion y definicion de variables, en este caso 'a' es la declaracion y '8' es la definicion.
a = 8
b = 3
c = a + b

print(c)

# lo que se imprime sale 11, por que al declarar += significa que el primer valor al declarar y definir la variables numero es 10, indica que va a sumar el valor que ya tiene más 1.
numero = 10;
numero += 1;

print(numero);

# Si quitamos la f y los corchetes al definir bienvenida, nos marcará un error por que es una cadena de texto, si intentamos concatenar igual marcará error

# f es para indicar un FString por lo que al estar dentro de corchetes indicara que es una variable y se esta integrando a la cadena de texto, toma un dato y lo convierte a texto.
nombre = 5
#concatenar con FStrings
bienvenida = f"Hola {nombre} ¿Cómo estás?"
del nombre
# 'del nombre' el operador 'del' funciona para eliminar datos que se almacenan en la memoria, hay que recordar que al declarar variables, estas se alojan en un espacio en la memoria
print(bienvenida)

nombre = 5
bienvenida = f"Hola {nombre} ¿Cómo estás?"
# busca ola en bienvenida, lo que va a mostrar en consola es un true, si declaramos un 'not in bienvenida' nos va a mostrar un false
print("ola" in bienvenida)