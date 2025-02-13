"""
Exercicios com funções

Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variavel e mostre o valor da variável.

Crie uma função fala se um número é par ou impar.
Retorne se o numero é par ou impar.
"""

# def somar(x,y,z):
#     x = 10
#     y = 11
#     z = x * y
#     print(z)

# print(somar())

# numero_inteiro = input("Digite um número inteiro: ")

# def parImpar(p,i):
#     if numero_inteiro % 2 == 0:
#         print("Seu número inteiro é par.")
#     else:
#         print("Seu número inteiro é ímpar.")

# parImpar() 
    

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)


def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f"{numero} é par"
    return f"{numero} é impar"

print(par_impar(2))
print(par_impar(10))
print(par_impar(15))
print(par_impar(21))
