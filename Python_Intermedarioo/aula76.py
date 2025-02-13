"""
Dicionarios em python (tipo dict)
Dicionarios são estruturas de dados do tipo par de "chave" e "valor".
Chaves podem ser consideradas como "indice" que vimos na lista e podem ser de tipo imutaveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionario.
Usamos as chaves - {} - ou a classe dict para criar dicionarios.
Imutaveis: str, int, float, bool, tuple
Mutável: dict, list
"""

# pessoa = {
#     'nome': 'Lucas Veras',
#     'sobrenome': 'Silva',
#     'idade': 18,
#     'altura': 1.78,
#     'enderecos': [
#         {'rua': 'tal tal', 'numero': 123},
#         {'rua': 'outra rua', 'numero': 321},
#     ],
# }

# print(pessoa['nome'])
# print(pessoa['sobrenome'])

# print()

# for chave in pessoa:
#     print(chave, pessoa[chave])

# pessoa = {}

# chave = 'nome'

# pessoa[chave] = "Lucas veras"
# pessoa['sobrenome'] = "silva"

# print[chave] = "Maria"

# del pessoa['sobrenome']
# print(pessoa)
# print(pessoa['nome'])

# if pessoa.get('sobrenome') is None:
#     print('Não existe')
# else:
#     print(pessoa['sobrenome'])

"""
Métodos uteis dos dicionaios em Python
len - quantas chaves
keys - iteravel com as chaves
values - iteravel com os valores
items - iteravel com chaves e valores
setdefault - adiociona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtem uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o ultimo item adicionado
update - atualiza um diocionario com outro
"""

# pessoa = {
#      'nome': 'Lucas Veras',
#      'sobrenome': 'Silva',
#      'idade': 900,
# }

# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# print(list(pessoa.items()))

# import copy

# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1,2],
# }

# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 9999

# print(d1)
# print(d2)

p1 = {
    'nome': 'Lucas Veras',
    'sobrenome': 'Silva',
}

print(p1.get('nome'))

nome = p1.pop('nome')
print(nome)
print(p1)
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)
p1.update({
    'nome': 'NOVOVALOR',
    'idade': 432
})

print(p1)