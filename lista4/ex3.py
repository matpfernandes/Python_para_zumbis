'''
Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos
pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.
'''
import random

def num_aleatorio(n):
    l = []
    for i in range(n):
        l.append(random.randint(1,100))
    return l

v1 = num_aleatorio(10)
v2 = num_aleatorio(10)
v3 = []

for i in range(10):
    v3.append(v1[i])
    v3.append(v2[i])

print('V1: ',v1)
print('V2: ',v2)
print('V3: ',v3)        
