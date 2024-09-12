#pp5
'''Parei na aula 8'''
#import math
'''Na linha 3 veja que é importado a biblioteca padrão do python "math"'''
#from math import sqrt
'''Na linha 5 é importado o método "sqrt" ou raiz quadrada da biblioteca math'''
#import random
'''Na linha 7 é importado a biblioteca "random" ou "aleatória" 
    .Ela possui métodos para definir numeros ou valores aleatórios para
    variáveis como abaixo'''
#r = random.random()
#print(r)
#k = rando.randint(0, 12)
#print(k)

#from math import trunc
'''O método trunc da biblioteca math remove as casas decimais do número'''
#ra = float(input('Digite um valor:'))
#print('A parte inteira do número digitado é; {}'.format(trunc(ra)))

#import math
#h = float(input('Digite um cateto:'))
#h2 = float(input('Digite outro cateto:'))
#h3 = ((h**2) + (h2**2))**(1/2)
#print('O valor da Hipotenusa é: {}'.format(h3))



#import math
#from math import cos, sin, tan
'''A biblioteca math possui os métodos seno, cosseno e tangente de um número
    .Para utilizar-las as variaveis devem ser, antes, transformadas em radianos;
    Para transformar em radianos utilize o método "randians()".'''
#a = float(input('Digite o valor do angulo:'))
#se = sin(math.radians(a))
#co = cos(math.radians(a))
#tan = tan(math.radians(a))
#print('Para o angulo de {}\nO seno vale {:.3f}\nO cosseno vale {:.3f}\nE a tangente vale {:.3f}'.format( a, se, co, tan))

import random
from random import randint
'''O método randint() escolhe um valor aleatório de uma lista ou tupla,que no caso é
    a tupla t'''
a = str(input('Digite o nome do aluno:'))
a2 = str(input('Digite o nome de outro:'))
a3 = str(input('Digite o nome de mais outro:'))
a4 = str(input('Digite o nome de um ultimo aluno'))
t = a, a2, a3, a4
g = random.choice(t)
print('O aluno sorteado foi {}'.format(g))


#import random
#from random import choice
'''O método choice escolhe um elemento aleatório para a lista escolhida'''
#a = str(input('Digite o aluno:'))
#b = str(input('Digite outro:'))
#c = str(input('Digite outro:'))
#d = str(input('Digite um ultimo:'))
#f = [a, b, c, d]
#print('0 aluno escolhido foi: {}'.format(random.choice(f)))




#import random
#from random import choice
#from random import shuflle
'''O método shuffle() ordena de forma aleatória elementos de uma lista'''
#a = str(input('Digite um aluno:'))
#a2 = str(input('Digite outro aluno:'))
#a3 = str(input('Digite outro:'))
#a4 = str(input('Digite mais outro:'))
#h = [a, a2, a3, a4]
#random.shuffle(h)
#print('A ordem escolhida foi:\n{}'.format(h))




#g = float(input('Digite um numero decimal:'))
#p = int(g)
#print('A parte inteira é:',p)


#import math
#from math import hypot
'''O método hypot(cateto_oposto, cateto_adjacente) calcula a hipotenusa;
    Para utiliza-lo ofereça dois parametros(variáveis), respectivamente: cateto_oposto
    e cateto_adjacente'''
#co = float(input('Digite o cateto oposto:'))
#ca = float(input('Digite o cateto adjacente:'))
#print('A hipotenusa vale: {}'.format(hypot(co, ca)))

