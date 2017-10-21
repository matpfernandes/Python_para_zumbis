v = []
n = 0
consoante = 0

while n < 10:
    c = input('Digite um caracter: ')
    v.append(c)
    if c not in 'aeiou':
        consoante += 1
    n += 1


print('Consoantes: ', consoante)
