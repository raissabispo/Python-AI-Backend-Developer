#Um método de classe é um método que está ligado à classe em si, e não a uma instância específica da classe
#Um método estático é um método que não está ligado nem à classe nem à instância. Ele não usa a instância (como self) nem a classe (como cls) como seu primeiro parâmetro

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))