def mostrar_menu():
    print("\n=== Sistema de Persistência ===")
    print("1 - Salvar dado no Banco (ABC)")
    print("2 - Salvar dado na Nuvem (Protocol)")
    print("0 - Sair")

def executar_menu(storage_banco, storage_nuvem, func_formal, func_flexivel):
    while True:
        mostrar_menu()
        opcao = input("Onde deseja salvar? ")
        
        if opcao in ["1", "2"]:
            dado = input("Digite o dado a ser salvo: ")
            
            if opcao == "1":
                # Usa a função que exige herança da ABC
                func_formal(storage_banco, dado)
            elif opcao == "2":
                # Usa a função flexível que exige apenas o método do Protocol
                func_flexivel(storage_nuvem, dado)
                
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Escolha 1, 2 ou 0.")
