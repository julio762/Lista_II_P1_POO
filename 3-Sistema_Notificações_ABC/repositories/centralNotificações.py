
from notificador import Notificador

class CentralNotificacoes:
    def __init__(self):
        self.notificadores = []

    def adicionar_notificador(self, notificador: Notificador):
        self.notificadores.append(notificador)

    def enviar_para_todos(self, mensagem: str):
        print(f"\n--- Transmitindo Mensagem Centralizada ---")
        for n in self.notificadores:
            n.notificar(mensagem)
