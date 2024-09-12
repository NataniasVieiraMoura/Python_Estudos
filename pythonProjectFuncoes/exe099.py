cnt = 0
nmaior = 0
numero = []
qtd = 0
y = 6
from time import sleep


def t(x):
    print('Analizando os valores informados', end='')
    for x in range(0, y):
        print('.', end='')
        sleep(0.50)
    print('\n')


while True:
    qtd = int(input('Quantos valores deseja digitar? '))
    if qtd == 0:
        print(f'Você deseja informar {qtd} valores.\nO maior valor informado foi {qtd}')
    if qtd != 0:
        def maior(cnt, numero):
            print('-=' * 30)
            print(f'Voçe deseja informar {qtd} valores.')
            while cnt < qtd:
                cnt += 1
                numero.append(int(input(f'Digite o {cnt}ª número:  ')))
            numero.sort()
            numero.reverse()
            t(x = 0)
            print(f'O maior número é {numero[0]}')
            print('-=' * 30)
        maior(cnt, numero)
    prg = str(input('Continuar? (s/n)')).lower().strip()[0]
    while prg not in 'sn':
        print('Você digitou algo errado, tente novamente.')
        prg = str(input('Deseja continuar? (s/n)')).lower().strip()[0]
    if prg[0] == 'n':
        break
print('Fim')
