import urllib.request
import time

preco = 99.99

while preco >= 4.74:
    pagina = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
    text = pagina.read().decode('utf-8')
    onde = text.find('>$')
    inicio = onde + 2
    fim = inicio + 4
    preco = float(text[inicio:fim])
    if preco >= 4.74:
        time.sleep(600)
print('Comprar! Preço: %5.2f' %preco)
