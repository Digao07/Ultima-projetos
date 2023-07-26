import pytest
from exercicio3 import (
    ler_dimensoes_objeto,
    calcular_preco_volume,
    validar_medida,
    ler_peso_objeto,
    calcular_multiplicador_peso,
    ler_rota,
    calcular_multiplicador_rota,
    calcular_frete
)

def test_calcular_preco_volume():
    assert calcular_preco_volume(500) == 10.0
    assert calcular_preco_volume(5000) == 20.0
    assert calcular_preco_volume(15000) == 30.0
    assert calcular_preco_volume(50000) == 20.0

def test_validar_medida():
    assert validar_medida('100') == 100
    assert validar_medida('abc') == -1

def test_calcular_multiplicador_peso():
    assert calcular_multiplicador_peso(0.05) == 1.0
    assert calcular_multiplicador_peso(0.5) == 1.5
    assert calcular_multiplicador_peso(5) == 2.0
    assert calcular_multiplicador_peso(15) == 3.0

def test_calcular_multiplicador_rota():
    assert calcular_multiplicador_rota('rs') == 1.0
    assert calcular_multiplicador_rota('bs') == 1.2
    assert calcular_multiplicador_rota('br') == 1.5

def test_calcular_frete():
    assert calcular_frete(1000, 1.5, 1.2) == 1800.0
    assert calcular_frete(5000, 2.0, 1.0) == 10000.0
    assert calcular_frete(20000, 3.0, 1.5) == 90000.0