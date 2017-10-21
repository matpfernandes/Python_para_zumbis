#Faça um Programa que leia três números e mostre o maior deles

a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))

if a>=b and a>=c:
    maior = a
elif b>=c:
    maior = b
else:
    maior = c

print("Maior: %d" %maior)
