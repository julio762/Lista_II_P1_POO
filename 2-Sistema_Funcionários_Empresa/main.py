from empresa import Empresa
from funcionario_assalariado import FuncionarioAssalariado
from funcionario_horista import FuncionarioHorista
from funcionario_comissionado import FuncionarioComissionado

if __name__ == "__main__":
    minha_empresa = Empresa("Tech Solutions Manaus")

    f_assalariado = FuncionarioAssalariado("Ana Silva", "123.456.789-00", 5000.00)
    f_horista = FuncionarioHorista("Carlos Sousa", "987.654.321-11", 40, 50.00)
    f_comissionado = FuncionarioComissionado("Beatriz Lima", "456.123.789-22", 30000.00, 5.0)

    minha_empresa.adicionar_funcionario(f_assalariado)
    minha_empresa.adicionar_funcionario(f_horista)
    minha_empresa.adicionar_funcionario(f_comissionado)

    minha_empresa.listar_funcionarios()
    minha_empresa.mostrar_folha_pagamento()
