from armazenador import Armazenador
from typing import Any

class ArmazenadorBanco(Armazenador):
    def salvar(self, dado: Any):
        print(f"[ABC - Banco] Executando INSERT para persistir: {dado}")
