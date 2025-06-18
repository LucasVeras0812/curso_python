frase = "O Python é uma linguagem de programação"\
    "multiparadgima" \
    "Python foi criado por Guido Van Rossum"

i = 0

apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''


while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    if letra_que_apareceu_mais_vezes <= letra_que_apareceu_mais_vezes:
        apareceu_mais_vezes = letra_que_apareceu_mais_vezes
        apareceu_mais_vezes = quantas_vezes_letra_apareceu

    i += 1

print("A letra que apareceu mais vezes foi"
      f"{letra_que_apareceu_mais_vezes} que apareceu"
      f"{apareceu_mais_vezes}x")