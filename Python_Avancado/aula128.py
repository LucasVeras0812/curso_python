# Métodos de classe + factories (fábrica)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instancia no primeiro
# parametro, receberemos a própria classe.
class Pessoa:
    ano = 2025 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anonima', idade)

p1 = Pessoa('Lucas', 21)
p2 = Pessoa.criar_com_50_anos('Mariazinha')
p3 = Pessoa.criar_sem_nome(21)
p4 = Pessoa.criar_sem_nome(26)

print(p4.nome, p4.idade)
print(p3.nome, p3.idade)
print(p2.nome, p2.idade)

# print(Pessoa.ano)
# Pessoa.metodo_de_classe()