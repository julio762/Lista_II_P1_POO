
from notificador import Notificador

class NotificadorApp(Notificador):
    def notificar(self, mensagem: str):
        print(f"[Push Notification] Exibindo na tela do smartphone: '{mensagem}'")
