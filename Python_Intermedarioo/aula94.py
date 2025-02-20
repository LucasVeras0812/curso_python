#Try, except, else e finally

try:
    print("Abriu o arquivo")
    # 8/0
except ZeroDivisionError:
    print("Dividiu por zero")
else: # será executado quando não der erro
    print("Não deu erro")
finally: # sempre será executado
    print("Fecha o arquivo")


