from abc import ABC, abstractmethod
from typing import Any

class Armazenador(ABC):
    @abstractmethod
    def salvar(self, dado: Any):
        pass
