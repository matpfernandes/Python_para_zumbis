#calculo da fatorial com funcao

def fat_n(n):
    fat = 1
    while n > 0:
        fat = fat * n
        n = n - 1
    return fat

print(fat_n(10))
