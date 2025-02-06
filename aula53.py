"""
enumerate - enumera iteraveis (indices)
"""

lista = ['a', 'b', 'c']
lista.append("Joao")

lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)
