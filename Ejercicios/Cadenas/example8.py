#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

producto_precio = input("Introduce el precio del producto con dos decimales: ")
print(producto_precio[:producto_precio.find('.')], 'euros y', producto_precio[producto_precio.find('.')+1:], 'centimos')

# producto_precio = input("Introduce el precio del producto con dos decimales: "): En esta línea, se le pide al usuario que introduzca el precio de un producto con dos decimales. El valor ingresado por el usuario se almacenará en la variable producto_precio.

# producto_precio.find('.'): La función find('.') se utiliza para encontrar la posición del primer punto decimal en la cadena almacenada en producto_precio. Esto se hace para separar los euros de los céntimos.

# producto_precio[:producto_precio.find('.')]: Esta parte del código toma una porción (subcadena) de la cadena producto_precio desde el principio hasta el índice justo antes del punto decimal. Esto nos da la parte de los euros del precio del producto.

# producto_precio[producto_precio.find('.')+1:]: Aquí se toma una porción de la cadena producto_precio desde el índice justo después del punto decimal hasta el final. Esto nos da la parte de los céntimos del precio del producto.

# print(producto_precio[:producto_precio.find('.')], 'euros y', producto_precio[producto_precio.find('.')+1:], 'centimos'): Finalmente, esta línea imprime la información obtenida en los pasos anteriores. Muestra los euros y céntimos del precio del producto en un formato legible para el usuario.