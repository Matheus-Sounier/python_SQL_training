class IssoAi:
    """
        Essa coisa é uma coisa muito legal, ela tem um nome e uma idade, e tem um método que mostra a idade no próximo ano, e outro método que mostra a idade atual.
    """

    
    def __init__(self, name: str, idade: int) -> None:
        self.name = name
        self.idade = idade


    def aniver(self) -> str:
        self.idade += 1
        return f"No próximo ano, {self.name} faz {self.idade} anos"

    def validador(self) -> str:
        if self.idade > 60:
            return f'Tem {self.idade} anos, é muito velho'
        elif self.idade > 18:
            return f'Tem {self.idade} anos, é adulto'
        elif self.idade >= 0: 
            return f'Tem {self.idade} anos, é criança'
        else:
            return f'Coloque um número válido para a idade'

    def mssg(self) -> str:
        return f"{self.name} tem {self.idade} anos"
    
    def __str__(self) -> str: 
        return f"{self.name} tem {self.idade} anos"
    
    def __repr__(self) -> str:
        return f"IssoAi(name='{self.name}', idade={self.idade})"
    
    def __getstate__(self):
        return f'Estado: name = {self.name}, idade = {self.idade}'

p1 = IssoAi("Matheus", 10)

# print(p1)
print(p1.__dict__)
print(p1.__doc__)
print(p1.__class__)
print(p1.__dict__)
print(p1.__getstate__())
print(p1.__repr__())

# print(p1.validador())

# print(p1.aniver())

