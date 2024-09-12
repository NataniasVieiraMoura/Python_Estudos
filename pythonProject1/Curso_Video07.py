'''Aula 9'''
fraze = str('       A formacão vegetal Brasileira é diversificada.       ')
#print(fraze.strip())
#print(fraze.lstrip())
#print(fraze.rstrip())
#print(fraze.find('a'))
#print(fraze.count('a'))
#print(fraze.lower())
#print(fraze.upper())
#print(len(fraze))
#print('Trabalho' in fraze)
#print(fraze.replace('formacão', 'Conposição'))
#print(fraze.split())
#print('@'.join(fraze))
#print(fraze.capitalize())
#print(fraze.title())
#print(fraze.rfind())

'''Atividade 9:'''


#soid = str(input('Digite seu nome:')).strip()
#print('Seu nome em maiúsculas:{}'.format(soid.upper()))
#print('Seu nome em minúsculas:{}'.format(soid.lower()))
#n = len(soid)
#h = soid.count(' ')
#y = n - h
#so = soid.split()
#sos = len(so[0])
#print('Seu nome têm {} letras.'.format(y))
#print('Seu primeiro é {} e têm {} letras'.format(so[0], sos))


#cos = int(input('Digite um número:'))
#cos = str(cos)
#print(cos.split())
#print('Unidade:{}\nDezena:{}\nCentena:{}\nMilha:{}'.format(cos[3], cos[2], cos[1], cos[0]))

#gha = str(input('Digite o nome da Cidade:')).title().strip()
#k = gha.split()
#print('O nome da Cidade começa com Santo?', 'Santo' in k[0])


#nome = str(input('Digite seu nome:')).strip().title()
#print('Há Silva no seu nome?{}'.format('Silva' in nome))


#cod = str(input('Digite uma frase:')).upper().strip()
#print('Essa frase possui {} letras A'.format(cod.count('A')))
#print('A primeira vez que A aparece é na posição {}'.format(cod.find('A') + 1))
#print('A ultima vez que A aparece é na posição {}'.format(cod.rfind('A') + 1))

#non = str(input('Digite Seu nome:'))
#non1 = non.split()
#print('Sr {}, seu último é {}'.format(non1[0], non1[len(non1) - 1]))


#import random
#from random import randint
#from time import sleep
'''Aula 10'''
#cont = int(input('Adivinhe o valor escolhido pelo\ncomputador emtre 0 e 5:'))
#conp = random.randint(0, 5)
#print('Processando...')
#sleep(3)
#if cont == conp:
#    print('*'*100)
#    print('Você vemceu\nComputador escolheu: {}\nVocê escolheu: {}'.format(cont, conp))
#    print('*'*100)
#else:
#    print('Você perdeu\nVocê escolheu: {}\nO computador escolheu: {}'.format(cont, conp))


#vel = int(input('Digite a velocidade do altomovel:Km'))
#if vel > 80:
#    print('Você foi multado em R${}\npor percorrer {}Km acima da maxima permitida'.format((vel - 80) * 7, vel - 80))
#else:
#    print('Você estava em velocidade permitida, tenha um bom dia!')
#print('Fim')


#nun = int(input('Digite um número inteiro:'))
#if 0 == nun%2:
#    print('{} é Par.'.format(nun))
#elif 1 == nun % 2:
#    print('{} é Impar'.format(nun))

#via = float(input('Quantos km de viagem foram percorridos:Km'))
#if via <= 200:
#    print('A viagem de {:.3f}Km vai custar R${:.3f}'.format(via, via * 0.50))
#elif via > 200:
#    print('A viagem de {:.3f}Km vai custar R${:.3f}'.format(via, via * 0.45))
#else:
#    print('Digite um número válido:')


#import datetime
#from datetime import date
#ano = int(input('Digite um ano e direi se é bissexto:'))
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#    print('Sim, {} é bissexto'.format(ano))
#else:
#    print('Não, {} não é bissexto'.format(ano))
#ann = date.today().year
#print('O ano atual é {}'.format(ann))

#a = int(input('Digite um valor:'))
#b = int(input('Digite outro valor:'))
#c = int(input('Digite outro valor:'))
#if a > b and a > c:
#    print('O número {} é maior que {} e {}.'.format(a, b, c))
#elif b > a and b > c:
#    print('O número {} é maior que {} e {}.'.format(b, a, c))
#elif c > a and c > b:
#    print('O número {} é maior que {} e {}.'.format(c, a, b))
#if a < b and a < c:
#    print('O número {} é menor que {} e {}.'.format(a, b, c))
#elif b < a and b < c:
#    print('O número {} é menor que {} e {}.'.format(b, a, c))
#elif c < a and c < b:
#    print('O número {} é menor que {} e {}.'.format(c, a, b))
#else:
#    print('Você pode ter digitado errado.')

#sal = float(input('Digite o seu salário atual:'))
#if sal > 1.250:
#    sal1 = (sal * 10)/100 + sal
#    print('Seu salário era de R${}, com almento de 10% ficará R${}'.format(sal, sal1))
#elif sal <= 1.250:
#    sal1 = (sal * 15)/ 100 + sal
#    print('Seu salario de R${} passará a ser R${} com o almento de 15%'.format(sal, sal1))
#else:
#    print('Você deve ter digitado errado.')

'''
l1 = int(input('Digite um lado:'))
l2 = int(input('Digite outro lado:'))
l3 = int(input('Digite outro lado:'))
if l1 + l2 > l3 and l1 - l2 < l3 and l3 < l2 + l1:
    print('. Sim. Esses lados formam um triângulo.')
else:
    print('Não. O triângulo para os dados digitados não existe.')
'''

'''Modelo de função:'''
def função(parametro1 = 220,para2 = "1987", para3 = True):
    lista = [parametro1,para2,para3]
    return lista
'''A função recebe paramentros que podem conter valores padrão'''
print(função())#Caso não seja declarado valores, os valores padrão serão utilizados
print(função(443,"2003", False))

'''Lambda'''
função_lambda = lambda parametro_1 = 130, par_2 = 40, par_3 = 2: parametro_1/ par_2 % par_3
print(função_lambda(20,2,3))
print(função_lambda())