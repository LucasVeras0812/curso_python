#Try, except, else e finally

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1212])
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido.')
except (TypeError, IndexError):
    print('TypeError ou IndexError')
except Exception:
    print('Erro desconhecido.')

print("Continuar")