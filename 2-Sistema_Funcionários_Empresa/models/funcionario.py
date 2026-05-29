
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self):
        print(f"Nome: {self.nome} | CPF: {self.cpf}")

    @abstractmethod
    def calcular_pagamento(self) -> float:
        pass
