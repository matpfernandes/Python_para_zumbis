'''
Considere a empresa de telefonia Tchau.
Abaixo de 200 minutos, a empresa cobra R$
0,20 por minuto.
Entre 200 e 400 minutos, o preço é R$ 0,18.
Acima de 400 minutos o preço por minuto
é R$ 0,15. Calcule sua conta de telefone
'''

minutos = int(input('Quantidade de minutos: '))

if minutos < 200:
    preço = 0.20
elif minutos <= 400:
    preço = 0.18
elif minutos <= 800:
    preço = 0.15
else:
    preço = 0.08

print("Total: R$%.2f" %(minutos * preço))
