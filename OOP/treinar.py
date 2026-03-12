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