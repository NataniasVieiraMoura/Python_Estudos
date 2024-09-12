#aas = str(input('Você é M\F:'))
#if aas in 'Mm':
#    print('Sim')
#else:
#    print('Não')


'''Esse outro comando abaixo não foi feito por mim'''


#somaidade = 0
#mediaidade = 0
#maioridadehomem = 0
#maisvelho = 0
#totmulher20 = 0
#for p in range(1, 2):
#    print('________{}ºPessoa________'.format(p))
#    nome = str(input('Nome: ')).strip()
#    idade = int(input('Idade: '))
#    sexo = str(input('Sexo [M\F] : ')).strip()
#    somaidade += idade
#    if p == 1 and sexo in 'Mm':
#        maioridadehomem = idade
#        maisveho = nome
#    if sexo in 'Mm' and idade > maioridadehomem:
#        maioridadehomem = idade
#        maisvelho = nome
#    if sexo in 'Ff' and idade < 20:
#        totmulher20 += 1
#mediaidade = somaidade / 4
#print('A idade média do grupo é {} anos.'.format(mediaidade))
#print('O homem mais velho é {} com {} anos de idade.'.format(maisvelho, maioridadehomem))
#print('Ao todo são {} mulhees com 20 anos de idade.'.format(totmulher20))




#import random
#from random import randint
#estado = False
#somador = jogador = pc = 0
#escolha = ''
#somador = jogador + pc
#contador = 0
#while estado == False:
#    jogador = int(input('Número de 0 a 5:  '))
#    escolha = str(input('Par ou Impar?  ')).strip().upper()[0]
#    pc = randint(0, 5)
#    if somador // 2 == 0 and escolha == 'P':
#        print(f'Acertou!!!\nPc escolheu{pc}\nVocê escolheu{jogador}')
#        contador += 1
#    elif somador // 2 == 1 and escolha == 'I':
#        print(f'Acertou!!\nPc escolheu{pc}\nVocê escolheu{jogador}')
#        contador += 1
#    else:
#        print('Perdeu, fim de jogo.')
#        estado = True #Ou  escrevo só break
#print(f'Estado{estado}\nSomador{somador}\nEscolha{escolha}\nJogador{jogador}\nPc{pc}\nContador{contador}')



#contador = somador = cont = 0
#flag = 7
#while True:
#    contador = int(input('Número:  '))
#    somador += contador
#    if contador == flag:
#        break
#    cont += 1
#print(f'Você digitou {cont} numeros\n. Somados dão {somador}')
#print('Fim!')



#print('\033[32m-----------------------\033[m')






















