'''
Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números
sortudos existem entre 18644 e 33087, incluindo os extremos?
Resposta: 7995
'''
c = 0

for n in range(18644,33087):
    if '2' in str(n) and '7' not in str(n):
        c += 1
print(c)
