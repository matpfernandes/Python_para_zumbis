#Faça um Programa que leia três números e mostre o maior e o menor deles.

a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))

if a>=b and a>=c:
    maior = a
elif b>=c:
    maior = b
else:
    maior = c

if a<=b and a<=c:
    menor = a
elif b<=c:
    menor = b
else:
    menor = c

print("Maior: %d\nMenor: %d" %(maior,menor))
