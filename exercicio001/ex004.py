'''Estrutura de repetição for'''
#from time import time

#for gta in range(1, 45):
#    print('Falha na operação..')
#print('Fim.')

#for gta in range(0, 6):
#    print(gta)

#for gta in range(1000, 0, -1):
#    print(gta)

#for gta in range(0, 12, 3):
#    print(gta)

#'''ainda na aula 13 do mundo 2 do curso em video pyton'''


#for chat in range(0, 10):
#    print('Você é fei')
#print('Acabou')



#for chow in range(1, 15,3):
#    print(chow)


#for cha in range(26, 0, -1):
#    print(cha)



#ini = int(input('Digite um número de partida:'))
#fin = int(input('Digite um número limite:'))
#pas = int(input('Digite o passo da contagem:'))
#for co in range(ini, fin + 1, pas):
#    print(co)
#print('Acabou!!!')



#for con in range(1, 10):
#    print('Olá')
#print('Fim')

#m = 0
#for tax in range(0, 5):
#    m = float(input('Digite um número:'))
#print(m)
#print('Akabou!')

#g = 0
#sot = 0
#for t in range(0, 4):
#    g = int(input('Digite um número:'))
#    sot += g
#print('A somatoria dos números digitados é {}'.format(sot))
#print('fim!')

'''Exercicios for:'''

#import time
#from time import sleep
#for tro in range(10, -1, -1):
#    print(tro, '!')
#    sleep(1)
#print('Som de fogos estourando!!!!')




#for trx in range(0, 51, 2):
#    print(trx, end=' ')
#print('Números pares até 50')
'''ou voce faz o de baixo'''


#for six in range(2, 51, 2):
#    print(six,end=' ')
#print('Números pares até 50')


#s = 0
#x = 0
#for xso in range(1, 501, 2):
#    if xso % 3 == 0:
#        s += xso #'''ou eu faço s = s + xso'''
#        x = x + 1
#print('A soma é {}'.format(s))
#print('A soma foi feita com {} números\nque são divisiveis por 3'.format(x))

'''Descubri a formula abaixo quando me perguntei como ele poderia repetir um número
e manter outro constante emquanto funciona e percebi que ele repete um laço, ou seja,
um número, o tanto de vezes que outro laço quizer!'''

#for t in range(0, 10, 1):
#    print('Começo do laço:')
#    for g in range(0, 10, 1):
#        print(t)

#r = 0
#for q in range(0, 11, 1):
#    print('Tabuada do {}'.format(q))
#    for e in range(0, 10, 1):
#        r = e * q
#        print('{} * {} = {}'.format(e, q, r))
#print('Fim')


#g = int(input('Digite um valor:'))
#print('Tabuada do {}'.format(g))
#for d in range(0, 11, 1):
#    print('{} * {} = {}'.format(g, d, g * d))



'''Essa segunda  que aparece abaixo 
é mais longa e não usa o conceito 
de laço de repetição.'''


#x = int
#y0 = 0
#y1 = 1
#y2 = 2
#y3 = 3
#y4 = 4
#y5 = 5
#y6 = 6
#y7 = 7
#y8 = 8
#y9 = 9
#y10 = 10
#for q in range(0, 11, 1):
#    r = q * y0
#    print('{} * {} = {}'.format(q, y0, r))
#for q in range(0, 11, 1):
#    r = q * y1
#    print('{} * {} = {}'.format(q, y1, r))
#for q in range(0, 11, 1):
#    r = q * y2
#    print('{} * {} = {}'.format(q, y2, r))
#for q in range(0, 11, 1):
#    r = q * y3
#    print('{} * {} = {}'.format(q, y3, r))
#for q in range(0, 11, 1):
#    r = q * y4
#    print('{} * {} = {}'.format(q, y4, r))
#for q in range(0, 11, 1):
#    r = q * y5
#    print('{} * {} = {}'.format(q, y5, r))
#for q in range(0, 11, 1):
#    r = q * y6
#    print('{} * {} = {}'.format(q, y6, r))
#for q in range(0, 11, 1):
#    r = q * y7
#    print('{} * {} = {}'.format(q, y7, r))
#for q in range(0, 11, 1):
#    r = q * y8
#    print('{} * {} = {}'.format(q, y8, r))
#for q in range(0, 11, 1):
#    r = q * y9
#    print('{} * {} = {}'.format(q, y9, r))
#for q in range(0, 11, 1):
#    r = q * y10
#    print('{} * {} = {}'.format(q, y10, r))


#somat = 0
#cnt = 0
#for num in range(0, 6, 1):
#    leia = int(input('Digite números:'))
#    if leia % 2 == 0:
#        somat += leia
#        cnt += 1
#print('A soma dos números pares é {}.'.format(somat))
#print('Você informou {} números pares.'.format(cnt))



#t1 = int(input('Digite o primeiro termo da PA:'))
#raz = int(input('Digite a razão da PA:'))
#for cox in range(0, 11, 1):
#    print('{}'.format(t1 + raz * cox), end='---')
#print('Acabou')


#cnt = 0
#dix = int(input('Digite um número:'))
#for k in range(1, dix + 1):
#    if dix % k == 0:
#        print('\033[31m', end='')
#        cnt += 1
#    else:
#        print('\033[35m', end='-')
#    print('{}'.format(k), end='-')
#print('\033[34m\nO número {} têm {} divisores \033[m'.format(dix, cnt))
#if cnt == 2:
#    print('\033[37mO número {} é primo.\033[m'.format(dix))
#else:
#    print('\033[36mO número {} não é primo.\033[m'.format(dix))




#non = str(input('Digite algo:')).strip().lower()
#chr = non.split()
#chr = ''.join(chr)
#xur = '' #'''Ou faz xur = [::-1]'''
#for lrt in range(len(chr) - 1, -1, -1):
#    xur += chr[lrt]
#if xur == chr:
#    print('Esse é um palindromo.')
#    print(xur, 'e', chr)
#else:
#    print('Não é palindromo.')
#    print(xur, 'e', chr)

#men = 0
#mai = 0
#import datetime
#from datetime import datetime
#print(datetime.today().year)
#for cac in range(1, 8):
#    se = int(input('Digite o ano de nacimento do {}º:'.format(cac)))
#    if datetime.today().year - se >= 21:
#        men += 1
#    else:
#        mai += 1
#print('São {} pessouas já são maiores de idade\ne {} pessouas não são maior de idade.'.format(men, mai))

#menor = 0
#maior = 0
#for f in range(1, 8):
#    pes = float(input('Digite o peso da {}º pessoa:'.format(f)))
#    if f == 1:
#        menor = pes
#        maior = pes
#    else:
#        if pes > maior:
#            maior = pes
#        if pes < menor:
#            menor = pes
#print('O maior peso foi de {}'.format(maior))
#print('O menor peso foi de {}'.format(menor))









