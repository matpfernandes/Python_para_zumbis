#escrever o mes de uma data em extenso 
data_nasc = (input("Digite a data de nascimento(dd/mm/aaa): "))

meses = ['janeiro','fevereiro','marco',
         'abril','maio','junho','julho',
         'agosto','setembro','outubro',
         'novembro','dezembro']

data_nasc = data_nasc.split('/')

print('%s de %s de %s' %(data_nasc[0],meses[int(data_nasc[1])-1],data_nasc[2]))
