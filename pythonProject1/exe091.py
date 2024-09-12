from random import randint
from time import sleep
print('\033[34mDados rolando.\033[m',end='')
sleep(0.65)
for d in range(0, 6):
    print('\033[34m.\033[m', end='')
    sleep(0.5)
print()
lista = []
dic = {'1ª Jogador': randint(1, 6), '2ª Jogador': randint(1, 6), '3ª Jogador': randint(1, 6),
       '4ª Jogador': randint(1, 6)}
for k, v in dic.items():
    print(f'\033[31m    O {k} tirou {v}\033[m')
    lista.append(v)
    sleep(0.75)
print('\033[33;1m    == O ranking dos jogadores ==')
sleep(0.75)
lista.sort()
lista.reverse()
rpt = []
cnt = 0
for x in range(0, 4):
    for k, v in dic.items():
        if lista[x] == v and k not in rpt:
            rpt.append(k)
            cnt += 1
            print(f'O {cnt}ª lugar:    {k} tirou {v}')
            sleep(0.75)
print('Fim')
print('\033[m')




