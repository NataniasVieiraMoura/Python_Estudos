'''Funções 2
interactive help
docstrings
argumentos apcionais
escopos variáveis
help(...)'''
#help(input)
#print(input.__doc__)

'''Docstrings:'''


def contador(i, f, p):
    """



    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: nada
    """
    #Acima você explica a fucao que criou
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('Fim')


contador(1, 30, 4)
help(contador)


def sub(x = 0, y = 0, z = 0):
    """

    :param x:número para a conta
    :param y: número para a conta
    :param z:número para a conta
    :return: nada
    escreve a subtração dos valores
    """
    s = x - y - z
    print(f'A subtração vale {s}')


sub(5,2)
sub(1)
sub(8,1,4)
sub()
sub(z = 23, x = 2)
#help(sub)


def teste():
    x = 21
    print(x)

teste()#<= O x só existe localmente no def
#print(x)#<=dessa forma o x não existe porque foi declarado localmente no def
'''Se uma variável for declarada
fora de de uma def, ela existe para todo o
programa(exite globalmente), mas se eu
declarar um variável apenas no def, ela vai
existir apenas para o def, mas não vai existir 
globalmente.'''

e = 3


def exe(b):
    d = 7
    b += 3#variavel local
    c = 9#variavel local
    print(f'A recebe {a}')
    print(f'B recebe {b}')
    print(f'C recebe {c}')
    print(f'D recebe {d}')
    print(f'E recebe {e}')


a = 2#variavel global
exe(a)

d = 4
'''Como foi criada um variável local 7 para d,
a variável global 4 para d torna-se a variável local 7 para d, não a
global 4 para d'''

'''variaveis b e c (locais), não podem ser 
declaradas fora do escopo def exe(b): porque
só existem localmente '''


n1 = 10
print(f'O n1 global vale {n1}')


def funcao(n1):
    n1 = 3
    print(f'O n1 local vale {n1}')


funcao(n1)








def x(z):
    z+=10
    print(f'Q vale {q}')
    print(f'Z vale {z}')


q = 2
x(q)


def w(ex):
    global r
    ex+=3
    print(f'r vale {r}')
    print(f'ex vale {ex}')


r = 2
w(r)


'''Retorno de valores'''
def mult(a = 0, b = 0, c = 0):
    m = a * b * c
    return m# essa funcao retorna apenas os resultados


x1 = mult(2, 2, 1)
print(mult(5, 4, 2))
print(x1)


def fatorial(num = 1):
    resposta = 1
    for c in range(num, 0, -1):
        resposta *= c
    return resposta


x = int(input('Digite um número : '))
print(f'O fatorial de {x} é {fatorial(x)}')




def inpar(i = 0):
    if i % 2 == 1:
        return True
    else:
        return False


i = int(input('Digite um número: '))
if inpar(i):
    print('INPAR')
else:
    print('Par')