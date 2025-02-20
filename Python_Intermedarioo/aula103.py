# Funções decoradoras e decoradores
# Decorar = Adicionar / Removar / Restringir / Alternar
# Funções decoradoras são as funções que decoram outras funções
# Decoradores são usados para fazer o Python
# Usar as funções decoradoras em outras funções.

def criar_funcao(func):
    def interna(*args, **kwargs):
        print("Vou te decorar")
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f"O resultado foi {resultado}")
        print("Ok, agora voce foi decorado")
        return resultado
    return interna

def inverta_string(string):
    return string[::1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    
inverte_string_checando_parametro = criar_funcao(inverta_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)
