import pytest

from exercicio1 import calcular_valor_total_com_desconto

def test_calcular_valor_total_com_desconto():
    valor_unitario = 10.0
    quantidade = 10

 
    valor_sem_desconto_esperado = 100.0
    valor_com_desconto_esperado = 95.0

    valor_sem_desconto, valor_com_desconto = calcular_valor_total_com_desconto(valor_unitario, quantidade)


    assert valor_sem_desconto == valor_sem_desconto_esperado
    assert valor_com_desconto == valor_com_desconto_esperado