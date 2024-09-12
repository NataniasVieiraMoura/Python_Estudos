from time import sleep


def mostrador(i):
    print(i, end=' => ')#Para evitar o buffer de tela usa depois do end='' o ,flush=True
    sleep(0.75)


def estrso(i, p):
    while i < f:
        mostrador(i)
        i = i + p
    print(i, '.')


def estrsu(i, p):
    while i > f:
        mostrador(i)
        i = i - p
    print(i, '.')

def contador(i, f, p):
    print('\033[33m-=' * 10)
    print(f'Contagem de {i} até {f} de {p} em {p} :')
    if p > 1:
        print('?')
        if i < f:
            estrso(i, p)
        if i > f:
            estrsu(i, p)
    elif p < 0 and i > f:
        print('!')
        if i > f:
            while i > f:
                mostrador(i)
                i = i + p
            print(i)
    elif p == 1:
        print('@')
        if i < f:
            estrso(i, p)
        else:
            estrsu(i, p)
    if p < 0 and i < f:
        print('Esse laço não é possivel.')



i = int(input('Qua o inicio da contagem? '))
f = int(input('Qual o fim da contagem? '))
p = int(input('De quanto em quanto devo contar? '))
if p == 0:
    p = 1
contador(i, f, p)


print('\033[m')



'''Essa é uma forma de inverter o sinal de um número'''
#if x < 0:
#    x *= -1