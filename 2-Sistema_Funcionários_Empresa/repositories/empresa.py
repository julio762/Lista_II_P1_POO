
from funcionario import Funcionario

class Empresa:
    def __init__(self, nome: str):
        self.nome = nome
        self.lista_funcionarios = []

    def adicionar_funcionario(self, funcionario: Funcionario):
        self.lista_funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\n--- Cadastro Geral de Funcionários da {self.nome} ---")
        for f in self.lista_funcionarios:
            f.mostrar_dados()

    def mostrar_folha_pagamento(self):
        print(f"\n--- Folha de Pagamento - {self.nome} ---")
        total_folha = 0.0
        for f in self.lista_funcionarios:
            pagamento = f.calcular_pagamento()
            print(f"Funcionário: {f.nome} | Valor Devido: R$ {pagamento:.2f}")
            total_folha += pagamento
        print(f"--> Total da Folha: R$ {total_folha:.2f}")
