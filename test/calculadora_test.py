import sys
from faker import Faker
sys.path.append('C:/_python_projetos_/python-testes-unitarios')
from classes.calculadora import Calculadora
from adicao_spy import AdicaoSpy
from subtracao_spy import SubtracaoSpy

faker = Faker()

def test_adicao():
    adicao_spy    = AdicaoSpy()
    subtracao_spy = SubtracaoSpy()
    calculadora   = Calculadora(adicao_spy, subtracao_spy)
    numero1       = faker.unique.random_int()
    numero2       = faker.unique.random_int()

    resultado = calculadora.add(numero1, numero2, True)

    # teste entrada
    assert adicao_spy.soma_atributos['numero1'] == numero1
    assert adicao_spy.soma_atributos['numero2'] == numero2
    
    # teste saida
    assert resultado is not None


def test_adicao_none():
    adicao_spy    = AdicaoSpy()
    subtracao_spy = SubtracaoSpy()
    calculadora   = Calculadora(adicao_spy, subtracao_spy)
    numero1       = faker.unique.random_int()
    numero2       = faker.unique.random_int()

    resultado = calculadora.add(numero1, numero2, False)

    # teste entrada
    assert adicao_spy.soma_atributos == {}
    
    # teste saida
    assert resultado is None