#verificar se uma palavra é palindroma
palavra = input('String: ')

if palavra == palavra[::-1]:
    print("%s é palindroma" %palavra)
else:
    print("%s não é palindroma" %palavra)
