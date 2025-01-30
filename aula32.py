"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero_interiro = input("Digite um número inteiro: ")

# if type(numero_interiro) != int:
#     print("Você nao digitou um numero inteiro.")
#     if numero_interiro % 2 == 0:
#         print("Seu número inteiro é par.")
#     else:
#         print("Seu número inteiro é ímpar.")

# entrada = input("Digite um numero: ")

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = "impar"

#     if par_impar:
#         par_impar_texto = "par"

#     print(f"O numero {entrada_int} é {par_impar_texto}")
# else:
#     print("Você nao digitou um numero inteiro!")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# horario = int(input("Qual é a hora? "))

# if horario >= 0 and horario <= 11:
#     print("Bom dia!")
# elif horario >= 12 and horario <= 17:
#     print("Boa tarde!")
# elif horario >= 18 and horario <= 23:
#     print("Boa noite!")
# else:
#     print("Madrugada!")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

first_name = str(input("Whats your first name? "))

if len(first_name) <= 4:
     print("Your name is short!")
elif len(first_name) >= 5 and len(first_name) <= 6:
     print("Your name is normal!")
else:
     print("Your first name is big!") 