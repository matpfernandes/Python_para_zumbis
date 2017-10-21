soma = 0
while True:
    x = int(input('Digite o numero(0 sair): '))
    if x == 0:
        break
    soma = soma + x
print('Soma: %d' %soma)
