"""
Argumentos nomeados e não nomeados em funções python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor) 
"""


def soma(x, y, z):
    #Definição
    print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)


soma(1,2,34)
soma(x = 2, y= 4, z = 6)

print(1,2,3, sep="L")