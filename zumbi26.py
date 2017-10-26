#gerando lista de 15 numeros aleatorios de 10 a 100 sem repetição na lista
import random

def num_aleatorio(n):
    i = 0
    l = []
    while i < n:
        num = random.randint(10,100)
        if num not in l:
            l.append(num)
            i+=1
    l.sort()
    return l

print(num_aleatorio(15))
