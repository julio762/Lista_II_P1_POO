def mostrar_menu():
    print("\n=== Plataforma UFAM Play ===")
    print("1 - Listar todas as mídias")
    print("2 - Reproduzir todas as mídias")
    print("0 - Sair")

def executar_menu(plataforma):
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            plataforma.listar_midias()
        elif opcao == "2":
            plataforma.reproduzir_todas()
        elif opcao == "0":
            print("Encerrando UFAM Play...")
            break
        else:
            print("Opção inválida. Tente novamente.")
