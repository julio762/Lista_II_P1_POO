
from notificador import Notificador

class NotificadorSMS(Notificador):
    def notificar(self, mensagem: str):
        print(f"[SMS] Enviando torpedo para celular: '{mensagem}'")
