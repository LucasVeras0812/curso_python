import sys

# generator expression, iterables e iteratos em python
iterable = ['Eu', 'tenho', '__iter__']
iterator = iterable.__iter__() # __iter__ e __next__

lista = (n for n in range(10))
generator = [ n for n in range(10)]

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
