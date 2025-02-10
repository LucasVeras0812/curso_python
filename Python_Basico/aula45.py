"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entra o proximo valor
iter -> me entregue seu iterador
"""

# texto = "Lucas".__iter__()
# texto = iter("Lucas")      ## faz a mesma coisa


# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

# print(next(texto)) ## faz a mesma coisa
# print(next(texto)) ## faz a mesma coisa
# print(next(texto)) ## faz a mesma coisa
# print(next(texto)) ## faz a mesma coisa
# print(next(texto)) ## faz a mesma coisa

# print(texto)


text = "Luiz"           #iteravel
iterador = iter(text)   #iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

