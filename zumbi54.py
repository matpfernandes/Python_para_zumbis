from zumbi55 import *
import zumbi56
import zumbi57

itens = ['Esfirra', 'Coxinha', 'Pastel','Pão de queijo']
precos = [1.50, 2.20, 1.80, 1.20]
rodando = True

while rodando:
    opcao = 1
    for escolha in itens:
        print(str(opcao) + ". "+escolha)
        opcao = opcao + 1
    print(str(opcao) + ". Finalizar")
    escolha = int(input("Escolha uma opção: "))
    if escolha == opcao:
        #escolheu a ultima opcao finalizar
        rodando = False
    else:
        cartao = input('Número do  cartão de crédito: ')
        preco = zumbi56.desconto(precos[escolha - 1])
        if itens[escolha - 1] == 'Pastel':
            preco = zumbi57.desconto(preco)
        salva_transacao(preco, cartao, itens[escolha - 1])
