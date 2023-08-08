#Principio de sustitución de Liskov
# class Ave:
#     def volar(self):
#         return "Estoy volando"

# class Pinguino(Ave):
#     def colar(self):
#         return "No puedo volar"

# def hacer_volar(ave = Ave): #variable de parametro
#     return ave.volar()

# print(hacer_volar(Pinguino))

class Ave:
    pass

class AveVolador(Ave):
    def volar(self):
        return "Estoy volando"

class AveNoVolador(Ave):
    pass

# este principio hace referencia a que todo lo que haga la clase base, lo hagan sus clases derivadas, cada subclase tendra propiedades(no todas) que cumpla con lo que requiere para su funcionalidad, legibilidad y extensibilidad