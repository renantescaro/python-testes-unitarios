from faker import Faker

faker = Faker()

class AdicaoSpy:
    def __init__(self) -> None:
        self.soma_atributos = {}

    def soma(self, numero1, numero2):
        self.soma_atributos['numero1'] = numero1
        self.soma_atributos['numero2'] = numero2

        return faker.unique.random_int()