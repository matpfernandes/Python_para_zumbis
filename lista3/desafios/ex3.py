#Verifique se um inteiro positivo n é primo.

num = int(input("Digite um numero: "))

if num > 1:
    count = 1
    primo = 1
    while count < num:
        if num % count == 0:
            primo += 1
            count += 1
            if count > 2:
                break
        else:
            count += 1
    if primo > 2:
        print("Não é primo")
    else:
        print('Primo')
else:
    print('Primo')
