#Faça um programa que calcule o aumento de um salário.
#Ele deve solicitar o valor do salário e a porcentagem do aumento.
#Exiba o valor do aumento e do novo salário

salario = float(input('Digite o salario: '))
aumento = int(input('Aumento(%): '))

novo_salario = salario+(salario*(aumento/100))

print('Novo salario: ', novo_salario)
