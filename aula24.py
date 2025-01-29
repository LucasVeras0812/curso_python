# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 
#  L u c a s
# -5-4-3-2-1 

# nome = "Lucas"

nome = input("Digite o seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")

# print('a' in nome)
# print('z' in nome)
# print('uca' in nome)
# print(nome[0])
# print(nome[1])
# print(nome[2])
# print(nome[3])
# print(nome[4])