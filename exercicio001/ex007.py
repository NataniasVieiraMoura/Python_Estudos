
''' Exercicicos WHile
Exercicio 61: '''

#pa = 0
#raz = 0
#termo = 0
#contador = 0
#from time import sleep
#while contador != 10:
#    if contador == 0:
#        print('{}{}{}'.format('\033[35;40m', '§'*100, '\033[m'))
#        sleep(1)
#        termo = int(input('Digite o primeiro termo: '))
#        sleep(1)
#        raz = int(input('Digite a razão da PA: '))
#        print('{}{}{}'.format('\033[35;40m', '§'*100, '\033[m'))
#    pa = termo + raz * contador
#    contador += 1
#    sleep(1)
#    print('O {}ªtermo é {}'.format(contador, pa))
#print('{}{}{}'.format('\033[35;40m', '§'*100, '\033[m'))
#sleep(1)
#print('Fim')
#print('{}{}{}'.format('\033[35;40m', '§'*100, '\033[m'))


'''Exercicios 62: '''

#pa = 0
#termo = 0
#raz = 0
#contador = 0
#maxi = 11
#per = 1
#while contador != maxi and per != 0:
#    if contador == 0:
#        print('{}{}{}'.format('\033[35;40m', '§'*100, '\033[m'))
#        termo = int(input('Digite o primeiro termo: '))
#        raz = int(input('Digite a razão: '))
#        print('{}{}{}'.format('\033[35;40m', '§'*100, '\033[m'))
#    pa = termo + raz * contador
#    contador += 1
#    if contador == maxi:
#        print('{}{}{}'.format('\033[35;40m', '§'*100, '\033[m'))
#        per = int(input('Quantos termos mais você quer ver: '))
#        maxi = contador + per
#    if per != 0:
#        print('O {}ª termo é {}'.format(contador, pa))
#print('{}{}{}'.format('\033[35;40m', '§'*100, '\033[m'))
#print('O progama finalizou com {} termos apresentados.'.format(contador - 1))
#print('Fim!')
#print('{}{}{}'.format('\033[35;40m', '§'*100, '\033[m'))


'''Exercicio 63:'''

#t = 0
#a = 1
#x = 0
#y = 0
#z = 1
#cont = 0
#print('-'*20)
#t = int(input('Digite número: '))
#print('-'*20)
#r = t - 1
#while cont != t:
#     if cont == 0:
#         print(x, '-->', end='')
#         cont = cont + 1
#     elif cont == 1:
#         x = y + z
#         print(x, '-->', end='')
#         cont = cont + 1
#     elif cont == 2:
#         x = y + z
#         print(x, '-->', end='')
#         x = 1
#         y = 1
#         z = 1
#     if cont != t :
#         x = y + z
#         print(x, end='-->')
#         z = y
#         y = x
#         cont += 1
#print('Fim')


'''Exercicio 64'''

#contador = numero = somador = flag = 0
#while numero != 999:
#    numero = int(input('Digite um número[Desligar digite 999]:  '))
#    contador += 1
#    if numero == 999:
#        flag = contador - 1
#        somador -= 999
#    somador += numero
#flag = contador - 1
#print('Você digitou {} número que somados dão {}'.format(flag, somador))

'''Exercicio 64 do guana: '''

#cont = soma = num = 0
#flag = 999
#num = int(input('Digite um número: '))
#while num != flag:
#    soma += num
#    cont += 1
#    num = int(input('Digite um número: '))
#print('Você digitou {} números que somados dão {}'.format(cont, soma))

'''Exercicio 65'''

#contador = 0
#somador = 0
#numero = 0
#maior = 0
#menor = 0
#media = 0
#continuar = 'S'
#binar = 0
#bit = 0
#while binar == 0:
#    numero = int(input('Digite um número: '))
#    somador += numero
#    contador += 1
#    if contador == 1:
#        maior = numero
#        menor = numero
#    if numero > maior:
#        maior = numero
#    if numero < menor:
#        menor = numero
#    continuar = str(input('Quer continuar?Sim ou Não'))
#    continuar = continuar.strip().capitalize()
#    continuar = continuar[0]
#    if continuar == 'S':
#        binar = 0
#    elif continuar == 'N':
#        binar = 1
#if binar == 1:
#    media = somador / contador
#print('.Você digitou {} numeros\n.O mairo número digitado foi {}.\n.O menor número digitado foi {}.\n.A soma dos números digitados é {}.\n.A média dos números digitados é {:.3f}.'.format(contador, maior, menor, somador, media))
#print('Fim')