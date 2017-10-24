'''
Dados dois números inteiros positivos,
determinar o máximo divisor comum entre eles
usando o algoritmo de Euclides
'''


a = int(input('a: '))
b = int(input('b: '))

while a%b != 0:
    c = a%b
    a = b
    b = c
print('MDC = %d' %b)
