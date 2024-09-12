from time import sleep
def maior(*num):# * para receber vários valores
    cont = maior = 0
    print('\nAnalizando os valores indicados...')
    for x in num:
        print(x, end=' ')
        cont += 1
        if maior < x:
            maior = x
        sleep(0.2)
        print('Não há valores')
    print()
    print(f'Foram análizados {cont} números.O maior é {x}')


maior(2, 32, 4, 23)
maior(5, 12, 74, 3, 41, 0)


def negativo(q):
    print('\033[7m', q,'\n\033[m')


x = 'Folha'
negativo(f'Folha')
'''Para visualizar os marcadores: ctrl + f11'''
c = (
    '\033[m', #0 - sem cor
    '\033[31m', #1 - vermelho
    );

print(c[1], 'Frase', c[0])