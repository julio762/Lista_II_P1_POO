
from funcionario import Funcionario

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome: str, cpf: str, total_vendas: float, percentual_comissao: float):
        super().__init__(nome, cpf)
        self.total_vendas = total_vendas
        self.percentual_comissao = percentual_comissao

    def calcular_pagamento(self) -> float:
        return self.total_vendas * (self.percentual_comissao / 100)
