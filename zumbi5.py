#imprimir numeros pares de 0 até numero informado
fim = int(input("Digite o ultimo numero: "))

x = 1
while x <= fim:
    if (x % 2) == 0:
        print(x)
    x +=1
