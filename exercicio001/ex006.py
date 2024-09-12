'''While'''

#n = 1
#while n != 0:
#    n = int(input('Digite um valor: '))
#print('Fim')


#r = 'S'
#n = 0
#while r == 'S' and n != 100:
#    n = int(input('Digite um número:'))
#    r = str(input('Digite S ou N\npara sim ou não: ')).strip().upper()
#    r = r[0]
#print('Fim')


#nun = 1
#par = impar = 0
#while nun != 0:
#    nun = int(input('Digite um número: '))
#    if nun % 2 == 0:
#        par += 1
#    else:
#        impar += 1
#print('Você digitou {} números pares e {} números impares.'.format(par, impar))
#print('Fim')

'''Execicios while 57'''

#sexo = ''
#x = 0
#while x != 1:
#    sexo = str(input('Digite seu sexo [M\F]: ')).strip().capitalize()[0]
#    if sexo == 'M' or sexo == 'F':
#        x = 1
#    else:
#        print('Algo digitado está errado, tente novamente.')
#print('Seu sexo foi armazenado como {} com sucesso.'.format(sexo))
#print('Fim')

'''exercicio 57 do guana:'''

#sexo = str(input('Digite seu sexo:  ')).strip().upper()[0]
#while sexo not in 'MmFf':
#    sexo = str(input('Digite um valor válido:  ')).strip().upper()[0]
#print('Seu sexo foi armazenado como {} com sucesso.'.format(sexo))


'''Execicio while 58'''

#import random
#from random import randint
#numero = 1
#jogador = 0
#contador = 0
#import time
#from time import sleep
#while jogador != numero:
#    numero = random.randint(0, 10)
#    jogador = int(input('Escolha um número de 0 a 10:'))
#    print('O computador escolheu', numero)
#    contador += 1
#    if numero != jogador:
#        if numero > jogador:
#            sleep(0.5)
#            print('Perdeu.')
#            sleep(1)
#            print('Mais... Tente novamente.')
#            sleep(0.5)
#        else:
#            sleep(0.5)
#            print('Menos...Tente novamente.')
#            sleep(1)
#    if jogador == numero:
#        sleep(0.5)
#        print('Finalmente venceu\nDepois de {} tentativas.'.format(contador))
#print('Fim')


'''exercicio 58 do guanab'''

#from random import randint
#computador = randint(0, 10)
#print('Olá eu sou o Pc e acabei de escolher um número.\n.Você consegue advinhar qual foi?')
#acertar = False
#palpites = 0
#placarh = 0
#placarm = 0
#while not acertar:
#    jogador = int(input('Qual é seu palpite? '))
#    palpites += 1
#    if jogador == computador:
#        acertar = True
#        placarh += 1
#    else:
#        placarm += 1
#        if jogador < computador:
#            print('Mais...Tente novamente.')
#        elif jogador > computador:
#            print('Menos...Tente novamente.')
#print('.Acertou com {} tentativas. Parabens!\n.Placar Homems: {} X Maquinas: {}.'.format(palpites, placarh, placarm))


'''Execicio 59'''


#escolha = 0
#nun1 = 0
#nun2 = 0
#op = ''
#while escolha != 5:
#    print('#'*30)
#    nun1 = int(input('Digite um número: '))
#    nun2 = int(input('Digite um outro número: '))
#    escolha = int(input('     [1]adição\n     [2]Multiplicação\n     [3]Maior\n     [4]Novos Números\n     [5]Sair do progama:  '))
#    print('$'*20)
#    if escolha == 1:
#        op = '+'
#        print(' {} {} {} = {}.'.format(nun1, op, nun2, nun1 + nun2))
#    if escolha == 2:
#        op = '*'
#        print(' {} {} {} = {}.'.format(nun1, op, nun2, nun1 * nun2))
#    if escolha == 3:
#        op = '>'
#        if nun1 > nun2:
#            print('{} {} {} = {}'.format(nun1, op, nun2, nun1))
#        elif nun2 > nun1:
#            print('{} {} {} = {}'.format(nun2, op, nun1 , nun2))
#        if nun1 == nun2:
#            op = '='
#        print('{} {} {} '.format(nun1, op, nun2))
#    if escolha == 4:
#        print('-'*20, 'RECOMEÇO', '-'*20)
#    if escolha > 5:
#        print('O numero {} não é válido.\nTente novamente.'.format(escolha))
#print('Fim do programa.!!!')

'''Exercicio 59 guanabara:'''


#escolha = ''
#nun1 = 0
#nun2 = 0
#op = ''
#soma = 0
#mult = 0
#div = 0
#sub = 0
#ig = '='
#import time
#from time import sleep
#print('#'*30)
#nun1 = int(input('Digite um número: '))
#nun2 = int(input('Digite um outro número: '))
#print('''    [+]adição
#    [*]Multiplicação
#    [-]Subtração
#    [/]Divisão
#    [>]Maior
#    [n]Novos Números
#    [0]Sair do progama.''')
#print('$'*20)
#while escolha != '0':
#    escolha = str(input('>>>>>Escolha:  '))
#    if escolha == '+':
#        op = '+'
#        soma = nun1 + nun2
#        print(' {} {} {} {} {}.'.format(nun1, op, nun2, ig, soma))
#    elif escolha == '-':
#        op = '-'
#        sub = nun1 - nun2
#        print('{} {} {} {} {}.'.format(nun1, op, nun2, ig, sub))
#    elif escolha == '*':
#        op = '*'
#        mult = nun1 * nun2
#        print(' {} {} {} {} {}.'.format(nun1, op, nun2, ig, mult))
#    elif escolha == '/':
#        op = '/'
#        div = nun1 / nun2
#        print('{} {} {} {} {}.'.format(nun1, op, nun2, ig, div))
#    elif escolha == '>':
#        op = '>'
#        if nun1 > nun2:
#            print('{} {} {} {} {}'.format(nun1, op, nun2, ig, nun1))
#        elif nun2 > nun1:
#            print('{} {} {} {} {}'.format(nun2, op, nun1, ig, nun2))
#        if nun1 == nun2:
#            print('{} {} {} '.format(nun1, ig, nun2))
#    elif escolha == 'n':
#        nun1 = int(input('Digite um número: '))
#        nun2 = int(input('Digite um outro número: '))
#        print('-'*20, 'RECOMEÇO', '-'*20)
#    elif escolha not in '/*-+0':
#        print('O numero {} não é válido.\nTente novamente.'.format(escolha))
#    sleep(0.5)
#    print('Finalizando.', end='')
#    sleep(0.5)
#    print('.', end='')
#    sleep(0.5)
#    print('.')
#    sleep(0.5)
#print('Fim do programa.!!!')


'''Exercicios 60'''

#import math
#from math import factorial
#numero = 1
#fat = 0
#contador = 0
#contador2 = 1
#while contador2 != 0:
#    if contador == 0:
#        numero = int(input('Digite um número: '))
#        contador = numero
#        print(contador, end='')
#    print(' X ', end='')
#    contador = contador - 1
#    print(contador, end='')
#    if contador == 1:
#        print(' = ', end='')
#        fat = factorial(numero)
#        print('{}'.format(fat))
#        contador2 = 0
#print('Fim')


'''Exercicio 60 do guana:'''

'''x -= 1
f *= c'''
