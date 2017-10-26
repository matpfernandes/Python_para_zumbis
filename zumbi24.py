#faça uma funcao que embaralhe as letras de uma string
import random

def embaralha(s):
    l = list(s)
    random.shuffle(l)
    return ''.join(l)

print(embaralha('matheus'))
