texto = "asldpqi cpaomlapw pwocp ixuapcmw puplajx xkl qpoeryl asfçks dhfggçpty paocpmq och ppqçapalzmxbvvmx pncnqmxbzmlaqp xmpqwre ppcqml apwoiru oti wepo ip qxmlxq pw oiqw pmxoqwl adfp"
def fatiamento(texto):
    dicionário = {}
    for y in set(texto):
        dicionário = {x: texto.count(x) for x in set(texto)}
        yield dicionário
        if True:
            return
'''for i in fatiamento(texto):
    print(i)
'''
import math
import random
lista = [x**2 for x in range(1,100) if x%3 == 0]
#print(lista)

lore = [x if x%2 == 0 else 0 for x in lista]
#print(lore)

cubos_quadrados = [x for x in lore if x%2 and x%3 != 0]
#print(cubos_quadrados)

limpo = lore.copy()
#print(lore)
limpo = set(limpo)
#print(limpo)
limpo.add("TEXTO QUALQUER")
limpo.add(True)
#print(limpo)
limpo.remove(True)
limpo.remove("TEXTO QUALQUER")
#print(limpo)
limpo.clear()
limpo.add("False")
#print(limpo)
limpo = set(x for x in range(1,100))
#print(limpo)
for x in range(1,80):
    limpo.pop()
#print(limpo)

from random import choice,randint
letras = "abcdefghijklmnopqrstuvwxyz"
numeros = "1234567890"
palavra = codigo = ""
nomes = []
nums = []
for y in range(6):
    for x in range(5):
        codigo += choice(numeros)
        palavra += choice(letras)
    nomes.append(palavra)
    nums.append(codigo)
    codigo = palavra = ""
#print(nomes)
#print(nums)

composto = [(nomes[x],nums[x]) for x in range(len(nomes))]
cod_aluno = {composto[x][0]:composto[x][1] for x in composto}
print(cod_aluno)



