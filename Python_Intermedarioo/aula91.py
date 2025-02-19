# introdução as generator functions em python
# generator = ( n for n in range(10))

def generator(n=10):
    yield 1
    print("continuando")
    yield 2
    print("...........")
    yield 3
    print("Acabou")

gen = generator(n=0)

for n in gen:
    print(n)
