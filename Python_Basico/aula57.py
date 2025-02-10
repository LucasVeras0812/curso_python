"""
Lista de listas e seus indices
"""
salas = [
    ['maria', 'helena'],

    ['lucas'],

    ['luiz', 'joao', 'edu']
]

print(salas)

for sala in salas:
    print(f"A sala é {sala}")
    for aluno in sala:
        print(f"Os alunos são {aluno}")