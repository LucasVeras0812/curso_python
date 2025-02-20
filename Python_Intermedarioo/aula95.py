# raise - lançando exceções (erros)

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Voce está tentando dividir por zero')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f"{n} deve ser int ou float"
            f"{tipo_n.__name__} enviado"
        )

def tratarErros(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
     
    return n / d

print(tratarErros(8,0))