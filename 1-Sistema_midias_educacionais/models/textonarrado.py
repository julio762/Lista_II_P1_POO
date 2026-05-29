
from midia import Midia

class TextoNarrado(Midia):
    def __init__(self, titulo: str, duracao: int, idioma: str):
        super().__init__(titulo, duracao)
        self.idioma = idioma

    def reproduzir(self):
        print(f"[Texto Narrado] Escutando a narração de '{self.titulo}' em {self.idioma}")
