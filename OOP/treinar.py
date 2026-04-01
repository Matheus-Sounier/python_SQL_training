# class Livros:
#     def __init__(self, nome, autor, paginas):
#         self.nome = nome
#         self.autor = autor
#         self.paginas = paginas

#     def get_paginas(self):
#         return self.paginas

# class Biblioteca:
#     def __init__(self, nome, capacidade):
#         self.nome = nome
#         self.capacidade = capacidade
#         self.livros = []

#     def add_livros(self, livro):
#         if len(self.livros) < self.capacidade:
#             self.livros.append(livro)
#             return True
#         return False

#     def get_media_paginas(self):
#         value = 0
#         for livro in self.livros:
#             value += livro.get_paginas()
#         return value / len(self.livros)

# l1 = Livros("monalisa", 'pedro cabral', 186)
# l2 = Livros("jipas", 'salomão pedroso', 145)
# l3 = Livros("sndfjaf", 'jorge saolo', 123)

# biblitequinha = Biblioteca('Seu vicente', 2)
# biblitequinha.add_livros(l1)
# biblitequinha.add_livros(l2)
# biblitequinha.add_livros(l3)
# print(biblitequinha.get_media_paginas())

# class ContaBancaria:
#     def __init__(self, titular, saldo, inicial):
#         self.titular = titular
#         self.saldo = saldo
#         self.inicial = inicial

#     def get_saldo(self):
#         return self.saldo
    
# class Conta:
#     def __init__(self, nome, capacidade):
#         self.nome = nome
#         self.capacidade = capacidade
#         self.contas = []

#     def abrir_conta(self, conta):
#         if len(self.contas) < self.capacidade:
#             self.contas.append(conta)
#             return True
#         return False
    
#     def get_saldo_total(self):
#         value = 0
#         for i in self.contas:
#             value += i.get_saldo()
#         return value

#     def buscar_conta(self, titular):
#         pass
        

# c1 = ContaBancaria('fudido', 123456, 126768)
# c2 = ContaBancaria('legal', 123123, 112321)

# continha = Conta('matheus', 2)
# continha.abrir_conta(c1)
# continha.abrir_conta(c2)
# print(continha.get_saldo_total())


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I'm a {self.name} and I'm {self.age} years old")

class Cat(Pet):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color= color

    def speak(self):
        print('meow')

    def show(self):
        print(f"I'm a {self.name}, i'm {self.age} years old and my color is {self.color}")

class Dog(Pet):
    def speak(self):
        print('bark')


p = Pet('matheus', 10)
p.show()

c = Cat('matheus', 10, 'black')
c.show()