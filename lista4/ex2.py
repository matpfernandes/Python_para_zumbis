'''
Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
números ímpares na lista IMPAR. Imprima as três listas.
'''
import random

def num_aleatorio(n):
    l =[]
    for i in range(n):
        l.append(random.randint(10,100))
    return l

l = num_aleatorio(20)
par = []
impar = []

for n in l:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print('Lista: ', l)
print('Pares: ', par)
print('Impares: ', impar)
