
from midia import Midia

class Plataforma:
    def __init__(self, nome: str):
        self.nome = nome
        self.lista_midias = []

    def adicionar_midia(self, midia: Midia):
        self.lista_midias.append(midia)

    def listar_midias(self):
        print(f"\nMídias Disponíveis na Plataforma {self.nome}")
        for midia in self.lista_midias:
            midia.mostrar_info()

    def reproduzir_todas(self):
        print(f"\nReprodução ({self.nome})")
        for midia in self.lista_midias:
            midia.reproduzir()
