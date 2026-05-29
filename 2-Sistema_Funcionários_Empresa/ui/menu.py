def mostrar_menu():
    print("\n=== Sistema de RH - Tech Solutions ===")
    print("1 - Listar funcionários cadastrados")
    print("2 - Mostrar folha de pagamento")
    print("0 - Sair")

def executar_menu(empresa):
    while True:
        mostrar_menu()
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            empresa.listar_funcionarios()
        elif opcao == "2":
            empresa.mostrar_folha_pagamento()
        elif opcao == "0":
            print("Fechando sistema de RH...")
            break
        else:
            print("Opção incorreta!")
