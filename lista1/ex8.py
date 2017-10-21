#Converta uma temperatura digitada em Fahrenheit para Celsius. F = 9*C/5 + 32

f = int(input('Digite a temperaturaem Celsius: '))

c = (f-32)*5/9

print('Fahrenheit: %.2f' %c)
