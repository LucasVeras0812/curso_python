# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy( que eu já vi)
# 0 0.0 '' False
# Tamb~em existe o tipo None que é
# usado para reresentar um não valor 


# entrada = input("[E] Entrar e [S] Sair: ")
# senha_digitada = input("Digite sua senha: ")

# senha_permitida = "123456"

#if condição:
#if True:
#....
# if (entrada == "E" or entrada == 'e') and senha_digitada == senha_permitida:
#     print("Entrou!")
# else:
#     print("Saiu!")


#Avaliação de curto circuito
senha = input("Digite sua senha: ") or print("Sem senha")
print(True or False)
#  print(True and 0 and True)