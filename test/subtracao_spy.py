from faker import Faker

faker = Faker()

class SubtracaoSpy:
    def __init__(self) -> None:
        self.diferenca_atributos = {}

    def diferenca(self, numero1, numero2):
        self.diferenca_atributos['numero1'] = numero1
        self.diferenca_atributos['numero2'] = numero2

        return faker.unique.random_int()