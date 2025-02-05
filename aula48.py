"""
Listas em python
Tipo list -> mutável
Suporta vários valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
métodos úteis: append, insert , pop, del, clear extend
"""

#            01234
#           -54321
# string =    "ABCDE"  # 5 caracteres
# lista = [123, True, "Lucas", 1.5]
# print(lista[1])
# print(bool(lista))
# print(lista, type(lista))

lista = [10,20,30,40,50,60]
print(lista)
lista[2] = 300
print(lista)
del lista[2]
print(lista)
print(lista[2])

lista2 = [1,2,3,4,5,6]
lista2.append(7) # adiciona um item na lista
print(lista2)

lista2.remove(7) # remove um item da lista
print(lista2)

lista2.pop() # remove o ultimo item da lista, podendo indicar o indice que quer remover
print(lista2)