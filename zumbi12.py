#calculo da fatorial de dn

i = 1
fat = 1
n = int(input("Digite o numero: "))

while i <= n:
    fat = fat * i
    i = i + 1
print('Fatorial(%d): %d' %(n,fat))
