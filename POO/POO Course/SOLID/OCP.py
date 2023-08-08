#Principio de abierto/cerrado
class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje por MAIL a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f'Enviando SMS a{self.usuario.sms}')

class NotificadorWhatsApp(Notificador):
    def Notificar(self):
        print(f'Enviando Whatsapp a{self.usuario.whatsapp}')

#El principio abierto/cerrado nos ayuda para evitar modificar la clase para poder extender funcionalidades
#sin embargo al cambiar la clase principal podríamos enfrentarnos a cambiarlo constantemente y no seria legible a largo plazo
#Para extender funcionalidades y agregar otras sin alterar la clase es creando otras clases que deriven de la clase padre y crear propiedades de instancia, objetos que son llamados de la clase padre para poder agregar nuevas funcionalidades sin modificar la clase padre