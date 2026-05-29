class Boleto:
    def __init__(self, codigo: str, valor: float):
        self.codigo = codigo
        self.valor = valor

    def imprimir(self):
        print(f"Boleto Bancário | Código: {self.codigo} | Valor: R$ {self.valor:.2f}")
