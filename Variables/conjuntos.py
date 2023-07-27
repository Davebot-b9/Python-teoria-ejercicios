#creando conjuntos con set
conjunto = set(["Dato1"]) # no es modificable

# metiendo un conjunto dentro de otro conjunto
conjunt1 = frozenset(["dato1", "dato2"])
conjunt2 = {conjunt1, "dato3"}

print(conjunt2)

#Teoria de conjuntos
conjunto1 = {1,2,3,4,5}
conjunto2 = {1,2,5}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
print(resultado)

#verificando si es un superconjunto
resultado2 = conjunto1.issuperset(conjunto2)
print(resultado2)


#vrificamos si hay algun numero en común
conjunto3 = {1,4,3,6}
conjunto4 = {2,9,7,8}

resultado3 = conjunto3.isdisjoint(conjunto4)
print(resultado3)