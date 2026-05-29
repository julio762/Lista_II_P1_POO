from armazenador import Armazenador
from salvavel import Salvavel
from typing import Any

def ejecutar_salvamento_formal(armazenador: Armazenador, dado: Any):
    armazenador.salvar(dado)

def ejecutar_salvamento_flexivel(objeto: Salvavel, dado: Any):
    objeto.salvar(dado)
