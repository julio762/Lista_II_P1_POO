from typing import Protocol, Any

class Salvavel(Protocol):
    def salvar(self, dado: Any) -> None:
        ...
