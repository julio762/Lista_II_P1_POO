from armazenador import Armazenador
from typing import Any

class ArmazenadorArquivo(Armazenador):
    def salvar(self, dado: Any):
        print(f"[ABC - Arquivo] Gravando dados no disco local: {dado}")
