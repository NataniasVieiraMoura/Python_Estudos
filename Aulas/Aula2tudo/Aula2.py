from typing import Counter

from numpy.f2py.symbolic import COUNTER

texto = "asdo oaisd oap qpwom coqwon vqpwc owc pqcwom zç lx xlmcqwo xlas nmsd asomcoanwmpc qpq owecn cwqom"

def função(texto):
    chars = []
    quantiti = []

    for c in texto:
        if not c in chars:
            chars.append(c)
            quantiti.append(1)
        else:
            index = chars.index(c)
            quantiti[index] += 1
    print(chars)
    print(quantiti)
    biblioteca = {}
    for i in range(len(chars)):
        biblioteca[chars[i]] = quantiti[i]
    return biblioteca
#função(texto)
#print(função(texto))

'''Abaixo eu uso set. Um tipo de lista que não aceita valores repetidos.
    Com ela pode-se adicionar valores sem a necessidade de remover valores repetidos.'''
'''Abaixo transformo ela em lista para fazer mais manipulações'''

def func_melhorada(texto):
    unicos = set()
    for c in texto:
        unicos.add(c)
    lista_unicos = list(unicos)
    quantiti = [texto.count(c) for c in lista_unicos]
    mochila = {}
    for i in range(1, len(lista_unicos)):
        mochila[lista_unicos[i]] = quantiti[i]
    return mochila
#print(f"Biblioteca com set: {func_melhorada(texto)}")


def fun3_melhor(texto):
    '''unicos = set()
    for c in texto:
        unicos.add(c)
    lista_unicos = list(unicos)'''
    '''O list compreheinsio substitui o  laço
    O set não permite adição de valores repetidos
    A lista serve para manipular o conjuto de valores'''
    unicos = list({c for c in texto})#uma lista recebe um set que recebe uma list comprehension
    quantiti = [texto.count(c) for c in unicos]
    mochila = {}
    for i in range(1, len(unicos)):
        mochila[unicos[i]] = quantiti[i]
    return mochila
#print(f"Biblioteca com set: {fun3_melhor(texto)}")



def fun4_melhor(texto):
    #unicos = list({c for c in texto})
    #como o python ve string como lista, se setar a string sobra apenas todos os valoes unicos da string
    quantiti = [(c,texto.count(c)) for c in set(texto)]
    '''mochila = {}
    for i in range(1, len(unicos)):
        mochila[unicos[i]] = quantiti[i]'''
    #return quantiti
    return dict(quantiti)#transforma o formato de tupas com pares de dados em chave-valor respectivamente
#print(f"Biblioteca com set: {fun4_melhor(texto)}")



def fun5_melhor(texto):
    '''quantiti = [(c,texto.count(c)) for c in set(texto)]
    return dict(quantiti)'''
    return dict([(c,texto.count(c)) for c in set(texto)])
#print(f"Biblioteca com set: {fun5_melhor(texto)}")



def fun6melhor(texto):
    #você pode retornar exibido já um dicionário com os pares de tupla da lista setando o texto
    return print(dict([(c,texto.count(c)) for c in set(texto)]))
#print(f"Biblioteca com set: {fun6melhor(texto)}")
#fun6melhor(texto)



def fun7melhor(texto):
    return print(dict([(c,texto.count(c)) for c in set(texto)]))
#fun7melhor(texto)

def fun8melhor(texto):
    return print({c: texto.count(c) for c in set(texto)})
fun8melhor(texto)

'''
from collections import Counter
def fun9melhor(texto):
    #{c: texto.count(c) for c in set(texto)}
    return Counter[texto]#O Counter é um método que deveria fazer isso, mas não funciona
print(fun9melhor(texto))
'''