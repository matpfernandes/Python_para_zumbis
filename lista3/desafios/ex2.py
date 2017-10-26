'''
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
nenhuma delas esteja em falta no caixa.
'''

total = int(input("Total: "))
pago = int(input("Pago: "))

troco = total - pago

_50 = troco / 50
_20 = (troco % 50) / 20
_10 = ((troco % 50) % 20) / 10
_05 = (((troco % 50) % 20) % 10) / 5
_02 = ((((troco % 50) % 20) % 10) % 5) / 2
_01 = ((((troco % 50) % 20) % 10) % 5) % 2


print("Troco\nR$ 50: %d\nR$ 20: %d\nR$ 10: %d\nR$ 05: %d\nR$ 02: %d\nR$ 01: %d\n" %(_50, _20, _10, _05, _02, _01))
