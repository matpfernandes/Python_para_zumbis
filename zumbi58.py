import pygame.mixer
sounds = pygame.mixer

sounds.init()

def espera_tocar (canal):
    while canal.get_busy():
        pass

certos = 0
errados = 0

opcao = int(input('Aperte 1)Certo 2 Errado e 0)Finalizar '))
while opcao !=0:
    if opcao == 1:
        s = sounds.Sound('GUI/correct.wav')
        espera_tocar(s.play())
        certos = certos + 1
    if opcao == 2:
        s2 = sounds.Sound('GUI/wrong.wav')
        espera_tocar(s2.play())
        errados = errados + 1
    opcao = int(input('Aperte 1)Certo 2 Errado e 0)Finalizar '))

print('Certos: ', certos, 'Errados: ', errados)
