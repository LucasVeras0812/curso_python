a = "A"
b = "B"
c = 1.1

string = "a={} b={} c={}".format(a, b, c)
formato = string.format(
    nome=a, nome2=b, nome3=c    
) # parametro nomeado 

print(string)
print(formato)