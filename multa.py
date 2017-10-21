#Se o carro estiver acima de 110km/h
#recebe multa de R$5 por km a mais

velocidade = int(input('Velocidade: '))

if(velocidade>110):
    print('Você foi multado!')
    multa = (velocidade-110)*5
    print('Multa: %d' %multa)
