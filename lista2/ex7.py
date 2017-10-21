'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
'''

metros_quadrados = int(input('Informe o tamanho em metros quadrados: '))

litros = metros_quadrados/3

if litros % 18 == 0:
    latas = (litros/18)
else:
    latas = (litros//18)+1

print("Latas: %d\nPreço: %.2f" %(latas, latas*80.0))
