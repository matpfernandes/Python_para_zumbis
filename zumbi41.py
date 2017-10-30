import random

sorteado = random.randint(1,100)
chute = 0

while chute !=  sorteado:
    g = input('Chute um numero: ')
    chute = int(g)
    if chute == sorteado:
        print('Você ganhou!')
    else:
        if chute > sorteado:
            print('Alto')
        else:
            print('Baixo')
print('Fim de jogo')
