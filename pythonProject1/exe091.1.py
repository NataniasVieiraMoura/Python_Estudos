from random import randint
from time import sleep
from operator import itemgetter
dic = {'1ª Jogador': randint(1, 6),
        '2ª Jogador': randint(1, 6),
        '3ª Jogador': randint(1, 6),
        '4ª Jogador': randint(1, 6)}
ranking = dict()
print('Valores sorteados')
for k, v in dic.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)# O 1 em itemgetter é ordem de chave. 0 é ordem de valores
print('-='*15)
print('Ranking dos jogadores:')
for n, l in enumerate(ranking):
    print(f'O {n+1}º lugar : {l[0]} com {l[1]}')
    sleep(1)