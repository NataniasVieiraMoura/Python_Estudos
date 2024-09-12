'''Aula 15 de pithon'''
'''while True'''
'''As f strings abaixo:'''
'''Elas funcionam colocando um f fora das aspas no inicio
e assim voce pode colocar a string armazenada diretamente
nas chaves'''

#numero = 23
#print(f'A variavel armazenou {numero}')

'''break interronpe o while'''

#n = soma = 0.0
#while True:
#    n = int(input('Digite número:  '))
#    if n == 999:
#        break
#    soma += n
#    print(f'{n:=^4}')
#print(f'A soma vale {soma:.2f}')#python 3.6+

''' abaixo aparece a forma antiga de apresentar
variáveis :'''

#print('O numero: %s , a soma: %d'% (numero, soma)) #python 2

'''  Flag Exercicio 66:  '''

#numero = contador = somador = 0
#while numero != 999:
#    numero = int(input('Digite um número:'))
#    if numero != 999:
#        somador += numero
#        contador += 1
#    else:
#        print('. Acabou.')
#print(f'A soma dos números digitados é {somador} \nVocê digitou {contador} numeros')


'''Tabuada Exercicio 67:'''

#numero = 0
#contador = 0
#limite = 11
#pergunta = 'x'
#while True:
#    if contador == 0:
#        numero = float(input('Que tabuada?  '))
#        if numero > 0:
#            print('''\033[33;44m''', '==='*30, '''\033[m''')
#            print(f'''\033[35;40m{numero} * {contador} = {numero * contador}\033[m¬¬¬¬¬¬¬¬''', end='')
#            print(f'''\033[32m{numero} / {contador} = Não é possivel dividir {numero} por 0.\033[m''')
#        contador = 1
#    if contador < 11 and numero > 0:
#        print(f'''\033[35;40m{numero} * {contador} = {numero*contador}\033[m¬¬¬¬¬¬¬''', end='')
#        print('''\033[32m{} / {} = {:.2f}\033[m'''.format(numero, contador, numero/contador))
#        contador += 1
#        pergunta = '  '
#    if contador == 11:
#        while pergunta not in 'sn':
#            print('''\033[33;44m''', '===' * 30, '''\033[m''')
#            pergunta = str(input('\033[31mDeseja continuar ou não?  \033[m')).strip().lower()[0]
#            pergunta = pergunta.strip().lower()[0]
#    if pergunta == 's':
#        contador = 0
#        print(f'''\033[33;44m''', '===' * 30, '''\033[m''')
#    if pergunta == 'n':
#        break
#    if numero < 0 or numero == 0:
#        while numero < 0 or numero == 0:
#            print('\033[31mNão é possivel cálcular com números negativos\nOu por zero.\033[m')
#            numero = int(input('Que Tabuada deseja ver?  '))
#print('Fim')

'''   Exercicio 68'''

#import random
#from random import randint
#estado = False
#somador = jogador = pc = contador = 0
#escolha = ' '
#somador = jogador + pc
#while estado == False:
#    escolha = ' '
#    jogador = int(input('\033[36mNúmero de 0 a 10:\033[m'))
#    while jogador > 11:
#        jogador = int(input('\033[36mDigite um número de 0 e 10:\033[m'))
#    while escolha not in 'PI':
#       escolha = str(input('\033[36mPar ou Impar?\033[m'))
#       escolha = escolha.strip().upper()[0]
#    pc = randint(0, 10)
#    somador = jogador + pc
#    print(f'\033[31mO Pc colocou {pc}\nVocê colocou {jogador}\033[m\n\033[34mA soma foi : {somador}\033[m')
#    if somador % 2 == 0 and escolha == 'P':
#        print(f'\033[33mAcertou!!!\nPc escolheu Impar\nVocê escolheu Par\033[m')
#        contador += 1
#    elif somador % 2 == 1 and escolha == 'I':
#        print(f'\033[33mAcertou!!\nPc escolheu Par\nVocê escolheu Impar\033[m')
#        contador += 1
#    else:
#        print('Perdeu, fim de jogo.')
#        estado = True #Ou  escrevo só break
#print(f'Fim de jogo, você perdeu.\nVocê venceu {contador} vezes\nO computador uma vez.')


'''Exercicio 69.'''

#questao = True
#nmulher = nhomem = contidade = 0
#pergunta = ' '
#sex = ' '
#while questao == True:
#    idade = int(input('\033[37;1m Digite sua Idade:  \033[m'))
#    sex = '  '
#    while sex not in 'mf':
#        sex = str(input('\033[36m Digite seu sexo:  \033[m')).strip().lower()[0]
#        sex = sex.strip().lower()
#        sex = sex[0]
#    print('{} {} {}'.format('\033[35;1m', '..'*25, '\033[m'))
#    if sex == 'f' and idade < 20:
#        nmulher += 1
#    elif sex == 'm':
#        nhomem += 1
#    if idade >= 18 and :
#        contidade += 1
#    pergunta = '  '
#    while pergunta not in 'sn':
#        pergunta = str(input('\033[32;1mDeseja continuar ou não?  \033[m')).strip().lower()[0]
#    if pergunta == 's':
#        questao = True
#    if pergunta == 'n':
#        questao = False
#print(f'\033[34;1mO cadastro possui {nhomem} Homens\n{nmulher} Mulheres menores de 20 anos\nE {contidade} maiores de 18 anos.\033[m')
#print('\033[30mFim.\033[m')

'''Exercicio 70.'''
#pmb = '  '
#nomepro = pergunta = '  '
#preco = maismil = maisc = maisb = contador = somador = 0
#print(' += '*10)
#print('\033[31;1mLoja do Sedex\033[m')
#print(' += '*10)
#while True:
#    print('{} {} {}'.format('\033[32m', '*'*30, '\033[m'))
#    nomepro = str(input('\033[33mQual o produto?\033[m  '))
#    preco = float(input('\033[34mQual o preço dele?\033[m  '))
#    contador += 1
#    somador += preco
#    if contador == 1:
#        maisc = maisb = preco
#        pmb = nomepro
#    if preco > maisc:
#        maisc = preco
#    if preco < maisb:
#        maisb = preco
#        pmb = nomepro
#    if preco > 1000:
#        maismil += 1
#    pergunta = '  '
#    while pergunta not in 'sn':
#        pergunta = str(input('\033[35;1mDeseja continuar ou não?\033[m')).strip().lower()[0]
#    if pergunta == 'n':
#        break
#        #continuar = False
#print('{:=^50}'.format('Fim do Programa'))
#print(f'\033[32;1mVocê efetuou {contador} compras.\nO valor das suas compras foi de R$ {somador}\nVocê fez {maismil} compra de mais de R$ 1000 reais\nSua compra mais barata foi {pmb} de R$ {maisb}\033[m')
#print('Fim!')

'''Exercicio 71.'''

#print('{} {} {}'.format('\033[33;1m', '_'*32, '\033[m'))
#print('''        \033[31;1mCaixa Eletronico\033[m''')
#print('{} {} {}'.format('\033[33;1m', '-'*32, '\033[m'))
#passo = True
#cinq = 0
#vinte = 0
#dez = 0
#um = 0
#contador = 0
#while passo == True:
#    contador += 1
#    if contador == 1:
#        print('\033[43m', '#' * 33, '\033[m')
#        saque = float(input('\033[34mQuanto deseja sacar?  R$\033[m'))
#    if saque - 50 >= 0:
#        saque -= 50
#        cinq += 1
#    elif saque - 20 >= 0:
#        saque -= 20
#        vinte += 1
#    elif saque - 10 >= 0:
#        saque -= 10
#        dez += 1
#    elif saque - 1 >= 0:
#        um += 1
#        saque -= 1
#    else:
#        passo = False
#if cinq > 0:
#    print(f'\033[1;32m{cinq} notas de R$ 50\033[m')
#if vinte > 0:
#    print(f'\033[1;32m{vinte} notas de R$ 20\033[m')
#if dez > 0:
#    print(f'\033[1;32m{dez} notas de R$ 10\033[m')
#if um > 0:
#    print(f'\033[1;32m{um} notas de R$ 1\033[m')
#print('\033[43m', '#'*33, '\033[m')
#print('\033[36mFim! Volte sempre.\033[m')






