'''Funções: '''
def l(): print('-='*30)


#Emtre o def e o programa tem que ter duas linhas vazias.
l()
print('    Curso em video    ')
l()
print('    Gustavo Guanabara ')
l()
print('    Curso de Python   ')
l()


def l2(sms):
    print('='*25)
    print(sms)
    print('='*25)


l2("    Curso em Video    ")





a = int(input('Digite um número:  '))
b =  int(input('Digite um número:  '))


def soma(a, b):
    r = a + b
    print(r)


def sub(a, b):
    r = a - b
    print(r)


def mult(a, b):
    r = a * b
    print(r)


def div(a, b):
    r = a / b
    print('{:.3f}'.format(r))


def pi(a, b):
     if a % 2 == 0:
         print(f'{a} é Par')
     else:
         print(f'{a} é Impar')
     if b % 2 == 0:
         print(f'{b} é Par')
     else:
         print(f'{b} é Impar')


soma(a, b)
sub(a, b)
mult(a, b)
div(a, b)
pi(a, b)


def media(x, y):
    r = (x+y)/2
    print(r)


media(y = 23, x = 10)
'''Assim eu especifico onde eu quero cada um'''



lista = []
cnt = 0
per = int(input('Deseja somar quantos números? '))
while cnt != per:
    lista.append(int(input(f'Digite o {cnt+1}ª número: ')))
    cnt += 1



def somal(lista):
    smt = 0
    for x in range(0, len(lista)):
        smt += lista[x]
    print(f'A somatoria dos números é {smt}')


somal(lista)


def r(*núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e ao todo são {tam} números.')


r(9, 6, 4, 1, 0)
r(9, 2, 0, 0, 1)
r(9, 0)
r(10, 4, 3)


lst = []
for x in range(0, 3):
    lst.append(int(input('Digite número: ')))


#def dobrar(lst):
#    lst2 = []
#    for x in range(0, 3):
#        lst[x] *= 2
#    print(lst)


def criard(lst):
    lst2 = []
    for x in range(0, 3):
        lst2.append(lst[x]*2)
    print(lst2)


print(lst)
criard(lst)
#dobrar(lst)




