def salva_transacao(preco, cartao_credito, descricao):
    file = open('transacoes.txt','a')
    file.write("%07d%16s%16s\n" %(preco * 100, cartao_credito , descricao))
    file.close()
