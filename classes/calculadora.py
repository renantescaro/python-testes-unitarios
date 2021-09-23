class Calculadora:
    def __init__(self, adicao, subtracao) -> None:
        self.adicao    = adicao
        self.subtracao = subtracao

    
    def add(self, numero1, numero2, operacao):
        if operacao:
            return self.adicao.soma(numero1, numero2)
        return None


    def sub(self, numero1, numero2, operacao):
        if operacao:
            return self.subtracao.diferenca(numero1, numero2)
        return None