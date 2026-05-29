class Etiqueta:
    def __init__(self, destinatario: str, endereco: str):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self):
        print(f"Etiqueta de Envio -> Destino: {self.destinatario} | Endereço: {self.endereco}")
