#mro es metodo de resolucion de orden
class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B,C):
    pass

d = D()

#d.hablar()

print(D.mro())

B.hablar(d)
#el recorrido de la clase que hereda de otra es simple, piensa que es un arbol jerarquico, lo que hace mro es precisamente recorrer el arbol segun se declare la herencia, en este caso al primero ejecutar D() si tiene el metodo hablar, lo imprime.
#En caso de que no contenga nada se pasa a la primera clase que se delcara para que herede sus metodo y propiedades en este caso es B(), si ve contiene el metodo hablar, lo imprime, en caso contrario pasa a la siguiente clase que se declaro en D() que en este caso es C() y asi sucesivamente.