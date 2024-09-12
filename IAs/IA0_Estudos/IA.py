'''Comentários: para acessar a lista de bookmark da linha digite:
shift + f11.'''
'''Para acessar a um bookmark digite Ctrl + caracter_do_bookmark(exemplo :1,2,3,a,b,c,...)'''
'''Aula 0 até a aula 13 da playlist curso_ia_python'''
#Comentários
#Lista em python:
lista = [1,2,3,4,5,6]
'''A contagem da lista é apartir do 0, depois 1,2,3,4...'''
produtos = [["Correia","Biela","Corrente"],["s1g65","6s5ds","6sg8s"],[15, 20,54]]
print(produtos[2][1])
print(produtos[0][2], produtos[1][0], produtos[2][2])
seleção = produtos
print(type(seleção))
seleção = produtos[0][1]
print(type(seleção))

import random
from random import choice, choices
cidades = ["Porto Alegre","Buriti dos Montes", "Uruçuí", "Altos", "Oeiras", "Marabá", "Íapoque", "Joenvile", "Pindamonhanguaba"]
print(len(cidades))
escolhido = choice(cidades)
ordenados = choices(lista)
print(escolhido)
print(f"choices {ordenados}")
a = lista
a.append(23)
'''append adiciona elemento na lista'''
print(a)
#abaixo crio outra lista
lista2 = [10,16,17]
#abaixo adiciona cada elemento da lista em outra lista
for item in lista2:
    a.append(item)
print(a)
num = 15
print(type(num))
num = 54.52
print(type(num))
x = [2, 4, 10, 16]
listay = []
for valor in x:
    listay.append(float(valor))
print(listay)
# o f no print serve para chamar variáveis dentro do texto
for dado in listay:
    print(f"{type(dado)} para {dado}")
#tupla: Lista que não pode ser alterada
estatica_l = (23,54,76)
print(estatica_l)
'''abaixo um exemplo de erro que não pode ser alterada'''
#estatica_l.append(243)
lis_54 = [1,2,3,4,5,6,7]
print(lis_54)
lis_54[0] = 999
print(lis_54)
del lis_54[4]#del elimina um elemento na posição indicada
print(lis_54)
tuplex = tuple(lis_54)
print(f"tuplex = {tuplex}")
'''No python quando uma tupla tem apenas um elemento coloque um virgula após o elemento para que o tipo tupla seja identificado'''
#Antes:
valor_69 = (15)
print(type(valor_69))#aqui ele não vai retornar que o valor é uma tupla
valor_69 = (15,)
print(type(valor_69))#aqui por causa da virgula o python entende que é um tupla
conbinado = (43)#não é tupla
conbinado = (43,)#é tupla
'''Dicionário = {}'''
contr = ["6d1gf","6f4g8","9dgfa98","s9d81fg"]
winklinks = {"Chave":"Valor",
             "Cod_pod": contr,
             "Sede": "Conpasso_Redondo_Rua: Doroteria_CEP:.2348-23"}
print(winklinks["Chave"])
print(winklinks["Cod_pod"][3])
print(winklinks["Sede"])
winklinks["Sede"] = "Dom Severino, Rua: Ricardo Mauricio, CEP:. 45543-34"
print(winklinks["Sede"])
winklinks["Chave"] = "Valor_1"
print(winklinks["Chave"])
print(winklinks.keys())#Chama todas as chaves do dicionário
print(winklinks.values())#Chama todos os valores no dicionário
wordww = {"tuplado": (23,543,65,345,234,54),
          "listado": ["Compasso articulado","Dedalo de ponta","Torquimetro manual","Rosca Rossy","Lamina de pressão"],
          "dic_interno": {15: "formula", 16: "Acidificante", 17: "emulsificante",18: "dentergente"}}
print(wordww.keys())
print(wordww.values())
'''Strings com python'''
fra_sim = "Estou gostando do curso"
print(fra_sim[0])
print(fra_sim[11:])
print(fra_sim[4:20:3])
print(fra_sim[10:20])
print(fra_sim[:19])
qntdde = len(fra_sim)
print(qntdde)
print(fra_sim.count("a"))
'''Palavra reservada def para criar fuções'''

def calculador(qr, code):
    qrcode  = qr**2 - code**3
    return qrcode
def recal(formador):
    formador = formador/2
    print(formador)
print(calculador(2, 4))
recal(calculador(2,4))

'''Função lanbda é uma forma resumida de cria uma função'''
import math
from math import floor
# para criar uma função lambda:
'''Digite o nome da função 
que vai receber lambda 
e em seguida digite os parametros
seguidos de dois pontos e logo após 
digite o comando'''
calque = lambda forno, arm, cont: forno/23+arm+cont-forno%(forno**-2)
print(floor(calque(2003,43,112)))

#Problema: criar um sistema que pede dados e retorna informação:
quiz = lambda  km,litros, consumo: [km/litros,consumo - (km/litros)]
print(quiz(100,200,250))

kmh = [56,23,62,42,35,15,100,74,54,86]
mph = []
for dado in kmh:
    mph.append(dado/1.61)
print(mph)
'''Função map() => Aplica um comjunto de dados á uma função'''
mph_new = []
'''Abaixo uma lista vai receber uma lista de elementos que passaram pela função lambda
O parametro bloco  recebe cada elemento da lista kmh e divide por 1,61'''
mph_new = list(map(lambda bloco : bloco/1.61,kmh))
'''pass a passo:
Cria nome;
Receba uma lista;
a lista recebe um map;
o map recebe uma lambda que usa um paramentro(bloco);
o parametro altera cada elemento da lista selecionada(kmh);
a lista selecionada vai ao final(kmh)'''
print(mph_new)
print('\033[7m\n\033[m')
'''List Comprehension'''
'''Cria uma lista com um laço'''
numerais = [x for x in range(1,11)]
print(numerais)
num_raiz_qdda = [r**-2 for r in numerais]
print(num_raiz_qdda)
num_raiz_cub = [r**-3 for r in numerais]
print(num_raiz_cub)
num_quad = ([r**2 for r in numerais])
num_cub = ([r**3 for r in numerais])
print(f"{num_quad}\n{num_cub}")
cracter = [letra for letra in "Contrução Cívil"]
print(f"\033[7m{cracter}\033[m")

