'''
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor
valor, sem usar as funções max e min.
'''
import random

def num_aleatorio(n):
    l =[]
    for i in range(n):
        l.append(random.randint(10,100))
    return l

l = num_aleatorio(10)

print(l)

maior = 0
menor = 100

for i in l:
    if i < menor:
        menor = i
    if i > maior:
        maior = i

print('Maior: %d\nMenor: %d' %(maior, menor))
