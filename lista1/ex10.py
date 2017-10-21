#Escreva um programa para calcular a redução do tempo de vida de um fumante.
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#Considere que um fumante perde 10 minutos de vida a cada cigarro,
#calcule quantos dias de vida um fumante perderá. Exiba o total de dias

#dia tem 1440 = 144 cigarros

cigarros = int(input('Quantidade de cigarros por dia: '))
anos = int(input('A quantos anos fuma: '))

perdido = (cigarros*anos*365)/144

print('Dias perdidos: %d' %perdido)
