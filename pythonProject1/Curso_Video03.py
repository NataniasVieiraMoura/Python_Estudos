#import math
#from math import ceil
'''ceil faz aredondamento de um número para cima'''
#from math import floor
'''floor faz um aredondamento para baixo'''
#from math import trunc
'''trunc elimina da virgula para trás do número'''
#from math import pow
'''pow transforma o número numa potência'''
#from math import sqrt
'''sqrt faz a raiz quadrada do número'''
#from math import factorial
'''factorial faz a fatoração do número'''
nux = float(input('Digite um número:'))
#red = ceil(nux)
#fox = floor(nux)
#rass = trunc(nux)
#numm = 2
#xoxu = pow(nux, numm)
#ssx = sqrt(nux)
#print('O aredondamento para cima do número é:{}'.format(red))
#print('O Aredondamento para menos do número é:{}'.format(fox))
#print('A parte inteira do número é: {}'.format(rass))
#print('O número {} elevado á {}º potência do número é {}'.format(nux, numm, xoxu))
#print('A raiz quadrada do número é: {}'.format(ssx))
'''Terminei na aula 8 do python mundo 1'''


print('Frases são compostos de verbos, adjetivos, substantivos, advérbios, e etc.')
frase ='Frases são compostos de verbos, adjetivos, substantivos, advérbios, e etc.'
'''Lembre que começa no 0 a contagem'''
print(frase[5:11])
'''Essa função acima ele vai escrever apartir do 5 caracterie até o 10'''
print(frase[7])
'''Acima ele escreve o caracterie desejado, no caso o 7°'''
print(frase[2:20:2])
'''Acima ele escreve da 2° até a 19°, pulando 2 em 2 caracteries'''
print(frase[40:])
'''Acima ele vai escrever do 40° caracterie até o fim do testo'''
print(frase[:10])
'''Acima ele vai escrever do inicio até o 10° caracterie'''
print(frase[36::2])
'''Acimam ele vai escrever do 36° até od fim e pulando de 2 em 2'''
print(len(frase))
'''Acima a função mostra quantos caracteries tem no dado armazenado'''
print(frase.count('G'))
print(frase.count('t'))
print(frase.count('.'))
'''Essa função conta quantas vezes essa string aparece no dado armazenado'''
print(frase.count('a', 10, 40))
'''Essa função eu posso escolher em que secção dos caracteries
 começar a contar, no caso acima eu escolhi do 10º caracterie até o 40°'''
print(frase.find('ad'))
'''Essa função indica onde começa a aparecer a string que vocês escolheu'''
print(frase.find('Xh'))
'''Acima quando você procurar e não existir a str que você procura
ele vai indicar -1'''
print(frase.rfind('t'))
'''Acima o  r no find indica que ele vai procurar da direita para a esquerda onde começa 
a str que você procura'''
print('força' in frase)
print('etc' in frase)
'''As duas acima são funções que avalia true or false para a str que você procura'''
print(frase.replace('etc', '....'))
'''A função acima troca a string que tem pela que você quer nessa ordem'''
print(frase.upper())
print(frase.lower())
'''Respectivamente as duas funçoes acima deixam upper = a frase maiúscula e lower = a frase minúscula'''
print(frase.capitalize())
'''Essa função deixa a frase capitularizada'''
print(frase.title())
'''Essa função capitulariza todas as palavras da frase'''
print(frase.strip())
'''Essa função elimina espaços do dois lados da frase'''
print(frase.lstrip())
'''Essa função elimima espaços da esquerda da frase'''
print(frase.rstrip())
'''Essa função elimina espaçoes da direita da frase'''
print(frase.split())
'''Essa função gera uma lista das palavras na frase apartir dos espaços entre elas'''
print('-'.join(frase))
'''A função acima separa as palavras com a str que você digitou'''
'''Terminei aqui na aula 9'''
