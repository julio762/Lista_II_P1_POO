
from funcionario import Funcionario

class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome: str, cpf: str, salario_mensal: float):
        super().__init__(nome, cpf)
        self.salario_mensal = salario_mensal

    def calcular_pagamento(self) -> float:
        return self.salario_mensal
