from q4_impressao.relatorio_simples import RelatorioSimples

def mostrar_menu():
    print("\n=== Fila de Impressão ===")
    print("1 - Criar e imprimir Relatório Rápido")
    print("0 - Sair")

def executar_menu(processar_impressao_func):
    while True:
        mostrar_menu()
        opcao = input("Selecione: ")
        
        if opcao == "1":
            titulo = input("Qual o título do relatório? ")
            # A UI coleta os dados, cria o objeto e envia para a função polimórfica
            relatorio = RelatorioSimples(titulo)
            processar_impressao_func(relatorio)
        elif opcao == "0":
            print("Saindo do sistema de impressão...")
            break
        else:
            print("Opção inválida.")
