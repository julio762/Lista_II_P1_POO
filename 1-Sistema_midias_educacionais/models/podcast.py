
from midia import Midia

class Podcast(Midia):
    def __init__(self, titulo: str, duracao: int, apresentador: str):
        super().__init__(titulo, duracao)
        self.apresentador = apresentador

    def reproduzir(self):
        print(f"[Podcast] Ouvindo '{self.titulo}', com o apresentador {self.apresentador}")
