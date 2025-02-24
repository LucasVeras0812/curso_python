# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - Iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - ORdem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')

pessoas = [
    'joao', 'joana', 'luiz', 'leticia',
]
camisetas = [
    ['preta', 'branca']
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
