#print('Bom Dia!')
#a = input(str('Digite uma frase:')).strip().upper()
#print(a)
#print(a.isnumeric())
#print(a.isalpha())
#print(a.isalnum())
#print(a.istitle())
#print(a.islower())
#print(a.isupper())
#print(a.isspace())
#print(a.isdecimal())
#print(a.isdigit())



#b = '    As sociedades Humanas são construidas com costumes.    '
#print(b)
#print(len(b))
#print(b.find('3'))
#print(b.rfind('4'))
#print(b.rstrip())
#print(b.lstrip())
#print(b.replace('sociedades', 'Nações'))
#print(b.lower())
#print(b.upper())
#print(b.capitalize())
#print('@'.join(b))
#print(b.split())
#print(b.title())

#print('Humanos' in b)
#print('Homens' in b)
#print('45' in b)

#print(b[:10])
#print(b[15:])
#print(b[5:12])
#print(b[14:20:2])
#print(b[20::3])
#print(b[0:21])
#print(b[26])


#import math
#from math import ceil
#from math import floor
#from math import pow
#from math import sqrt
#from math import trunc
#from math import factorial
#nume = 4.16
#print(pow(nume, 3))
#print(sqrt(nume))
#print(floor(nume))
#print(ceil(nume))
#print(trunc(nume))



#escolha = input(str('Digite um nome:')).strip().title()
#sexo = input(str('Digite seu sexo de nacimento\n(M)Masculino ou (F)feminino:'))
#if escolha == 'Maria' or escolha == 'João':
#    print('Nome comum esse tal de {}'.format(escolha))
#elif escolha == 'João' and sexo == 'Masculino' or sexo == 'M':
#    print('Seu nome tem duas partes Sr(a) {}'.format(escolha))
#else:
#    print('Seu nome é incomum Sr(a). {}'.format(escolha))
#print('Fim')


'''Abaixo estrutura de repetição FOR'''
#for com in range(1, 20):
#    print(com)

#for numpar in range(0, 19, 2):
#    print(numpar)

#for numin in range(1, 19, 2):
#    print(numin)

#import time
#from time import sleep
#for tem in range(10, 0, -1):
#    print(tem)
#    sleep(0.5)
#print('Som de fogos de Artificio')

#import time
#from time import sleep
#contador = 0
#somador = 0
#for laço in range(0, 101, 1):
#    if laço % 2 == 0:
#        sleep(0.5)
#        print('Esse sim')
#        somador += laço
#        contador += 1
#    else:
#        sleep(0.3)
#        print('Esse não')
#print(somador)
#print(contador)
#sleep(1)
#print('Fim')


'''Tabuada de Multiplicação'''
#import time
#from time import sleep
#p = int(input('De que número você quer\na tabuada de multiplicação:'))
#for l in range(0, 11, 1):
#    print('{} * {} = {}'.format(p, l, p*l))
#    sleep(0.3)
#sleep(1)
#print('FIM')


#import time
#from time import sleep
#'''Progressão Aritimetica:'''
#termo = int(input('Qual o primeiro termo dessa PA?'))
#sleep(1)
#raz = int(input('Qual a razão dessa PA?'))
#sleep(1)
#limite = int(input('Até que termo deseja ver a Pa?'))
#sleep(1)
#for n in range(0, limite + 1, 1):
#    print('{}'.format(termo + raz * n ))
#    sleep(0.5)
#sleep(1)
#print('FIM')





'''Numeros Primos'''

#contador = 0
#primo = int(input('Digite aqui um número'))
#for m in range(1, primo + 1, 1):
#    if primo % m == 0:
#        contador += 1
#if contador <= 2:
#    print('{} O número digitado é Primo.{}'.format('\033[34m', '\033'))
#elif primo % 2 == 0:
#    print('{} O número digitado é par.{}'.format('\033[36;42m', '\033'))
#else:
#    print('{} O número digitado é impar. {}'.format('\033[32:45m', '\033'))


'''palindromo ou capicua'''


#n1 = str(input('Digite uma palavra: ')).strip().lower()
#n2 = n1.split()
#n3 = ''.join(n2)
#n4 = ''
#print(n1,'\n',n2,'\n',n3,'\n',n4)
#for nx in range(len(n1) - 1, -1, -1):
#    n4 += n3[nx]
#if n1 == n4 :
#    print('A palavra {} digitada é palindromo.'.format(n1))
#else:
#    print('A palavra {} digitada não é palindromo.'.format(n1))



'''Maior idade(18 anos)'''


#import datetime
#from datetime import datetime
#maior = 0
#menor = 0
#for id in range(0, 7):
#    per = str(input('Digite seu nome: '))
#    per1 = int(input('Que ano você naceu?'))
#    if datetime.today().year - per1 < 18:
#        menor += 1
#    else:
#        maior += 1
#print('{} pessoas são maiores de idade.'.format(maior))
#print('{} pessoas são maiores de idade.'.format(maior))
#print('{} pessoas são menores de idade.'.format(menor))


'''Conparador de pesos'''



#maior = 0
#menor = 0
#for g in range(0, 4):
#    peso = float(input('Digite seu peso: '))
#    if peso > maior and peso > menor:
#        maior = peso
#    if g == 0: # g só é zero uma vez logo a condição só ocorrerá no inicio.
#         menor = peso
#    elif menor > peso:
#        menor = peso
#print('O menor peso é {}.'.format(menor))
#print('O maior peso é {}.'.format(maior))


'''Analizador completo.(Esse comando foi feito por mim.)'''

#import datetime
#from datetime import datetime
#somador = 0
#contador0 = 0
#contador1 = 0
#contador2 = 0
#contador3 = 0
#hmax = 0
#for f in range(1, 5):
#    print('-'*10, '{}{}º Pessoa{}'.format('='*5, f, '='*5), '-'*10)
#    nome = str(input('Qual seu nome? ')).strip().capitalize()
#    nac = int(input('Que ano você naceu? '))
#    idade = datetime.today().year - nac
#    sexo = str(input('Qual seu sexo (M) ou (F)? ')).upper().strip()
#    sexo = sexo[0]
#    somador += idade
#    contador0 += 1
#    if sexo == 'F' and idade < 20:
#        contador1 += 1
#    if sexo == 'M' and idade > hmax:
#        contador3 += 1
#        n1 = nome
#        hmax = idade
#somid = somador / contador0
#if contador0 <= 1:
#    print('Não é possivel calcular a média de idade de um grupo\nsem duas ou mais pessoas.')
#else:
#    print('A média de idade do grupo é  de {:.2f} anos.'.format(somid))
#if contador3 >= 1:
#    print('O Sr. {} é o homem mais velho do grupo com {} anos de idade.'.format(n1, hmax))
#if contador1 >= 1:
#    print('Nesse grupo existe {} mulher(es) menor(es) de 20 anos.'.format(contador1))


'''Esse outro comando abaixo não foi feito por mim'''

#somaidade = 0
#mediaidade = 0
#maioridadehomem = 0
#maisvelho = ''
#totmulher20 = 0
#for p in range(1, 5):
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




























