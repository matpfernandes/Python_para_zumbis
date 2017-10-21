#Faça um Programa que peça os três lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.


a = int(input("Digite o lado A: "))
b = int(input("Digite o lado B: "))
c = int(input("Digite o lado C: "))

#condição de existencia
if((b-c) < a and a < (b+c) and (a-c) < b and b < (a+c) and (a-b) < c and c < (a+b)):
    if a==b==c:
        triangulo = "Equilátero"
    elif a==b or a==c or b==c:
        triangulo = "Isósceles"
    else:
        triangulo = "Escaleno"

    print('Triangulo[%d-%d-%d]: %s' %(a,b,c,triangulo))
else:
    print('Condição de existência não satisfeita')
