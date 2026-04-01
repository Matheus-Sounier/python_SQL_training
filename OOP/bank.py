class ContaBancaria:
    """
    Envia dados de um usuário, verifica o deposito e saque feito 
    """
    def __init__(self, nome: str, id: int, saldo: float=0) -> None:
        self.titular = nome
        self.saldo = saldo
        self.id = id

    def depositar(self, valor_colocado: float) -> None:
        if valor_colocado < 0:
            raise f'Não é possível depositar valores negativos!'
        self.saldo += valor_colocado

    def sacar(self, valor_tirado: float) -> None:
        if valor_tirado >= self.saldo:
            raise f'Saldo atual: R${self.saldo:,.2f}, valor solicitado: R${valor_tirado:,.2f}, saldo insuficiente'
        self.saldo -= valor_tirado
        return self.saldo

    def __str__(self) -> str:
        return f'{self.titular} de id: {self.id}\nTem R${self.saldo:,.2f} reais'

c1 = ContaBancaria('Matheus', 2, 2302)
c1.depositar(100)
c1.sacar(3000)
print(c1)