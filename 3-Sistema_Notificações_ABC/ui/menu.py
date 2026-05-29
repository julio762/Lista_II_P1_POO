def mostrar_menu():
    print("\n=== Central de Notificações ===")
    print("1 - Escrever e enviar nova notificação geral")
    print("0 - Sair")

def executar_menu(central_notificacoes):
    while True:
        mostrar_menu()
        opcao = input("Opção: ")
        
        if opcao == "1":
            mensagem = input("Digite a mensagem que deseja transmitir: ")
            central_notificacoes.enviar_para_todos(mensagem)
        elif opcao == "0":
            print("Desligando central...")
            break
        else:
            print("Comando não reconhecido.")
