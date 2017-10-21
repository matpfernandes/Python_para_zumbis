notas = []
soma = 0
i = 1
while i <= 4:
    n = float(input('Nota: '))
    notas.append(n)
    soma += n
    i += 1
print('Notas: ', notas)
print('Media: %.2f' %(soma/4))
