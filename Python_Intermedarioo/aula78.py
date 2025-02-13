# 
# Sets - conjuntos em python (tipo set)
# Conjuntos são ensinados na matemática
# Representados graficamente pelo diagrama venn
# Sets em python são mutáveis, porem aceitam apenas tipos imutaveis como valor interno.
# tipos imutáveis como valor interno.

# Criando um set
# set(iteravel) ou {1, 2, 3}
# s1 = set() # vazio
# s1 = {'Lucas', 1,2,3} # com dados

# Sets são eficientes para remover valores duplicados de iteraveis
# - não aceitam valores mutaveis;
# - seus valores serão sempre unicos;
# - eles nao tem indexes;
# - eles nao garantem ordem;
# - eles são iteraveis(for, in, not in)

# l1 = {1,2,3,3,3,3,3,3,3,2,2,2,1,2} # com dados
# s1 = set(l1)
# l2 = list(s1)
# print(l1)

# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add("Lucas")
# s1.add(1)
# s1.update(("olá mundo", 1,2,3,4))
# #s1.clear()
# s1.discard("olá mundo")
# s1.discard("Lucas")
# print(s1)

# Operadores úteis:
# uniao | uniao (union) - une
# intersecção & (intersection) - itens presentes em ambos
# diferença - itens presentes apenas no set da esquerda
# diferença simétrica ^ - itens que nao estao em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3)
