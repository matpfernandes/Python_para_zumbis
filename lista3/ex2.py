'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

i = 0

while i == 0:
    user = input('Usuario: ')
    senha = input('Senha: ')
    if user == senha:
        print('Erro: usuario e senha iguais\n')
    else:
        i=1
