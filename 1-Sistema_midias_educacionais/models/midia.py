
from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo: str, duracao: int):
        self.titulo = titulo 
        self.duracao = duracao 

    
    def mostrar_info(self):
        print(f"Mídia: {self.titulo} | Duração: {self.duracao} min")

    @abstractmethod
    def reproduzir(self):
        pass
