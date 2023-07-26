import pytest
from exercicio2 import calcular_total_pedido

def test_calcular_total_pedido_com_item_invalido():
    codigo1 = 0
    total = 0.0
    total += calcular_total_pedido(codigo1)

def test_calcular_total_pedido_com_um_item():
    codigo1 = 101

    total = 0.0
    total += calcular_total_pedido(codigo1)

    assert total == 11.00

def test_calcular_total_pedido_com_dois_itens():
    codigo1 = 100
    codigo2 = 102

    total = 0.0
    total += calcular_total_pedido(codigo1)
    total += calcular_total_pedido(codigo2)

    assert total == 21.00

def test_calcular_total_pedido_com_todos_os_itens():
    codigo1 = 100
    codigo2 = 101
    codigo3 = 102
    codigo4 = 103
    codigo5 = 104
    codigo6 = 105
    codigo7 = 200
    codigo8 = 201

    total = 0.0
    total += calcular_total_pedido(codigo1)
    total += calcular_total_pedido(codigo2)
    total += calcular_total_pedido(codigo3)
    total += calcular_total_pedido(codigo4)
    total += calcular_total_pedido(codigo5)
    total += calcular_total_pedido(codigo6)
    total += calcular_total_pedido(codigo7)
    total += calcular_total_pedido(codigo8)

    assert total == 84.00

def test_calcular_total_pedido_com_cinco_itens_sendo_dois_com_mesmo_codigo():
    codigo1 = 100
    codigo2 = 101
    codigo3 = 100
    codigo4 = 103
    codigo5 = 104


    total = 0.0
    total += calcular_total_pedido(codigo1)
    total += calcular_total_pedido(codigo2)
    total += calcular_total_pedido(codigo3)
    total += calcular_total_pedido(codigo4)
    total += calcular_total_pedido(codigo5)

    assert total == 55.00