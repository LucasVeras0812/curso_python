<<<<<<< HEAD

x = 1


def escopo():
    global x
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        print(x,y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)
print(x)
print(x)
=======
"""
Escopo de funçoes em Python
Escopo significa o local onde aquele codigo pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel
O escolo local é o escopo onde apenas nomes do mesmo local
pode ser alcançados.
"""

>>>>>>> 8403520333fd3286b9bef3e227a6c7c5981f45ac
