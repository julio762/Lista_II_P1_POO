from typing import Any

class ArmazenadorNuvem:
    # Esta classe não herda explicitamente da ABC Armazenador
    def salvar(self, dado: Any):
        print(f"[Protocol - Nuvem] Enviando payload via API para servidor remoto: {dado}")
