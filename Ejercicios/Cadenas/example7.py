#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
e_mail = input("Introduce tu correo electronico: ")
print(e_mail[:e_mail.find('@')]+'@ceu.es')