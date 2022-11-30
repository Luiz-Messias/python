class Pessoa:
    def __init___(self, nome, idade, genero, altura):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.altura = altura

pessoa1 = Pessoa('Luiz', 18, 'Masc', 1.75)
pessoa2 = Pessoa('Maria', 28, 'Fem', 1.59)

print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)