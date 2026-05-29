from armazenador_arquivo import ArmazenadorArquivo
from armazenador_banco import ArmazenadorBanco
from armazenador_nuvem import ArmazenadorNuvem
from funcoes_salvamento import ejecutar_salvamento_formal, ejecutar_salvamento_flexivel

if __name__ == "__main__":
    print("--- Testando os Mecanismos de Persistência ---")
    
    storage_arquivo = ArmazenadorArquivo()
    storage_banco = ArmazenadorBanco()
    storage_nuvem = ArmazenadorNuvem()
    
    meu_dado = {"id": 1, "usuario": "alternei_brito"}

    print("\n>> Executando Salvamentos Formais (Baseados em ABC):")
    ejecutar_salvamento_formal(storage_arquivo, meu_dado)
    ejecutar_salvamento_formal(storage_banco, meu_dado)

    print("\n>> Executando Salvamentos Flexíveis (Baseados em Protocol):")
    ejecutar_salvamento_flexivel(storage_arquivo, meu_dado)
    ejecutar_salvamento_flexivel(storage_banco, meu_dado)
    ejecutar_salvamento_flexivel(storage_nuvem, meu_dado)
