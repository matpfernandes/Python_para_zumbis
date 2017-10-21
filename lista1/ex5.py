#Solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar.

preco = float(input('Digite o preço da merdoria: '))
desconto = int(input('Digite o desconto(%): '))

novo_preco = preco-(preco*(desconto/100))

print('Novo preço: ', novo_preco)
