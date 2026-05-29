
from notificador import Notificador

class NotificadorEmail(Notificador):
    def notificar(self, mensagem: str):
        print(f"[E-mail] Enviando para caixa de entrada: '{mensagem}'")
