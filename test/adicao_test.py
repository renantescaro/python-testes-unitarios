import sys
from faker import Faker
sys.path.append('C:/_python_projetos_/python-testes-unitarios')
from classes.adicao import Adicao

faker = Faker()

def test_soma():
    numero1   = faker.unique.random_int()
    numero2   = faker.unique.random_int()
    esperado  = numero1 + numero2
    resultado = Adicao().soma(numero1, numero2)
    assert resultado == esperado