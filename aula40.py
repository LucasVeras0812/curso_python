"""Calculadora com while"""

while True:
    num1 = input("Digite um numero: ")
    num2 = input("Digite um outro numero: ")
    operador = input("Digite um operador (+-/*): ")

    num_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        num_validos = True
    except:
        num_validos = None

    if num_validos is None:
        print("Um ou ambos os numeros digitados são inválidos.")
        continue

    operadores_perm = '+-/*'

    if operador not in operadores_perm:
        print("Operador inválido.")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue

    print("Realizando sua conta. Confira o resultado abaixo: ")

    if operador == "+":
        print(num1_float + num2_float)
    elif operador == "-":
        print(num1_float - num2_float)
    elif operador == "/":
        print(num1_float / num2_float)
    elif operador == "*":
        print(num1_float * num2_float)

    sair = input("Quer sair? ").lower().startswith('s')

    if sair is True:
        break
