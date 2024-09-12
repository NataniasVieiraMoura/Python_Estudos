'''Parei na metade da aula 3 do curso de python intermediário'''

#List comprehension consome muita memória se o loop for muito grande
#Gerador resolve esse problema
#O gerador só adiciona espaço na lista quando você necessitar
#Evita ter que alocar tanto espaço de uma vez
lista = [i for i in range(1_000_000)]#evite executar assim
#print(lista)
'''Para criar um gerador coloque a list comprehension emtre parentesis'''
#listager = (z for z in range(600_000_000))#gerador em list Comprehension
#for i in listager:
#    print(i)

#Outra forma de criar geradores:
'''
def arvore():#função
    n = 0#contador
    while(True):#loop
        n += 1#incremento
        yield n#gerador yield
for i in arvore():#como o for não tem condição e a função não tem parada
    #o código vai executar indefinidamente
    print(i)
'''

'''
def arvore():#função
    n = 0#contador
    while(True):#loop
        n += 1#incremento
        yield n#gerador yield
for i in arvore():#como o for não tem condição e a função não tem parada
    #o código vai executar indefinidamente
    print(i)
'''

def arvore(limite = 1025):
    n = 1
    while(True):
        n *= 2
        if n > limite:
            return#return encerra o loop do gerador
        yield n
'''for i in arvore():
    print(i)
   '''
def posição(limite=1025):#parametro
    r = 1
    while(True):
        r*= 3
        if r > limite:#condição de parada
            return
        yield r

def primos(teto = 200):
    y = 0
    while(True):
        y+=1
        if y%2 and y%3 != 0:
            yield y#yield é equivalente ao return do gerador
        if y > teto:
            return

'''
for w in primos():
    print(w)
'''

'''Combinando geradores'''

'''
def tratador(gerad,gerad2):#dois geradores em  uma função
    for q in gerad:
        yield q#retorna todos os valores de um gerador
    for h in gerad2:
        yield h#retorna todods os valores do outro gerador

for valor in tratador(arvore(), posição()):
    print(valor)
    '''
'''
def tratador2(gerad,gerad2):#dois geradores em  uma função
    yield from gerad#outra forma de iterar geradores
    yield from gerad2
for valor in tratador2(arvore(), posição()):
    print(valor)
'''

def tratador3(gerad,gerad2):#dois geradores em  uma função
    yield from gerad#outra forma de iterar geradores
    yield from gerad2
#requisitando valores do gerador
quadrado = arvore()
cubo = posição()
print(next(quadrado))
print(next(quadrado))
print(next(cubo))
