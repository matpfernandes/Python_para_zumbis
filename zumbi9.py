#calculo da soma de dez numeros inteiros

n = 1
soma = 0

while n <= 10:
    x = int(input('Digite o %d numero: ' %n))
    soma = soma + x
    n = n + 1
print('Soma: %d' %soma)
