# Problema dos parametros mutáveis em funçoes em python
def adiciona_clientes(nome, lista= None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('fernando', cliente1)
cliente1.append('')

cliente2 = adiciona_clientes('veras')
adiciona_clientes('cleber', cliente2)

cliente3 = adiciona_clientes('bate')
adiciona_clientes('beras', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
