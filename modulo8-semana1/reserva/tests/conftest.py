import pytest
from datetime import date
from model_bakery import baker
from reserva.models import Petshop, Reserva

@pytest.fixture
def reserva_fixture():    
    data = date(2022, 10, 1)
    return baker.make(
        Reserva,
        nome = 'Teste pytest',
        data = data,
        turno = 'Tarde'
    )   


@pytest.fixture    
def petshop():
    return baker.make(Petshop)