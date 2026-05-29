from boleto import Boleto
from etiqueta import Etiqueta
from relatorio_simples import RelatorioSimples
from processador import processar_impressao

if __name__ == "__main__":
    print("--- Processador de Impressão Estrutural (Protocol) ---")
    
    meu_boleto = Boleto("34191.79001 01043.513184", 250.50)
    minha_etiqueta = Etiqueta("Instituto de Ciências Exatas - ICET/UFAM", "Itacoatiara/AM")
    meu_relatorio = RelatorioSimples("Desempenho Acadêmico 2026/1")

    processar_impressao(meu_boleto)
    processar_impressao(minha_etiqueta)
    processar_impressao(meu_relatorio)
