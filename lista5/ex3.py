'''
Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também
divisíveis por 7?
Resposta: 183
'''
c = 0

for n in range(1067,3627):
    if n %2 == 0 and n % 7 == 0:
        c += 1

print(c)
