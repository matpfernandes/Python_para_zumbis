'''
Dizemos que um número natural é triangular se ele é produto de três números naturais
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n,
verificar se n é triangular
'''
n = int(input("Digite um numero: "))

i = 1

while i < n:
    if (i * (i+1) * (i+2)) == n:
        print("%d é triangular(%d,%d,%d)" %(n, i, i+1,i+2))
        break
    else:
        i+=1

if i >= n:
    print('%d não é triangulo' %n)
