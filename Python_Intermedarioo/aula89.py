# dir, hasattr e getattr em python
string = 'Lucas'
metodo = 'upper'

if hasattr(string, metodo):
    print("Exite upper")
    print(getattr(string, metodo)())
    print(string)