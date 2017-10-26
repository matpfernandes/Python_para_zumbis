gerando lista de 15 numeros aleatorios de 10 a 100 
import random

def num_aleatorio(n):
    l = []
    for k in range(15):
        l.append(random.randint(10,100))
    return l


print(num_aleatorio(15))
