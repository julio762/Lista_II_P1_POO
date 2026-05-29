from central_notificacoes import CentralNotificacoes
from notificador_email import NotificadorEmail
from notificador_sms import NotificadorSMS
from notificador_app import NotificadorApp

if __name__ == "__main__":
    central = CentralNotificacoes()

    email = NotificadorEmail()
    sms = NotificadorSMS()
    app = NotificadorApp()

    central.adicionar_notificador(email)
    central.adicionar_notificador(sms)
    central.adicionar_notificador(app)

    central.enviar_para_todos("Manutenção programada no sistema UFAM às 22h00.")
