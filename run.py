from classes.adicao import Adicao
from classes.subtracao import Subtracao
from classes.calculadora import Calculadora

calculadora = Calculadora(Adicao(), Subtracao())
op1 = calculadora.add(2, 5, True)
op2 = calculadora.sub(5, 3, True)

print(op1)
print(op2)