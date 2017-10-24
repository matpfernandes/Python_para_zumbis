#trocar as vogais de uma palavra por *

palavra = input('Digite uma frase: ')

i = 0
nova = ''
while i < len(palavra):
    if  palavra[i] in 'aeiou':
        nova+='*'
    else:
        nova += palavra[i]
    i+=1

print('Nova palavra: %s' %nova)
