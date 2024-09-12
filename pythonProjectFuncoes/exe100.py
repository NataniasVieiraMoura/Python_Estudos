lnumeros = []
from random import randint
from time import sleep


def sorteia(x):
    print(f'Os números sorteados foram: ', end=' [')
    for x in range(0, 5):
        sleep(0.65)
        lnumeros.append(randint(1, 10))
        print(f'{lnumeros[x]}', end='] -> [')
    print('\n')
def somaPar(y):
    soma = 0
    for y in range(0, 5):
        if lnumeros[y] % 2 == 0:
            soma += lnumeros[y]
    print(f'A soma dos pares é {soma}')



sorteia(x = 0)
somaPar(y = 0)

