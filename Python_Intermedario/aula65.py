"""
Introdução ás funções (def) em python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parametros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""

# def Print(a, b, c):
#     print("Várias1")
#     print("Várias2")
#     print("Várias3")
#     print("Várias4")

# def imprimir(a, b ,c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome="sem nome..."):
    print(f'Olá, {nome}')

saudacao("Lucas Veras!")
saudacao("Estefany Barcellos!")
saudacao()

