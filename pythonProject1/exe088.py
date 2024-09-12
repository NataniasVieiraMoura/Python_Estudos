from time import sleep
from random import randint
jogos = list()
num = 0
pgt = int(input(f'\033[34;1m Quantos jogos você quer que eu sortei?\033[m'))
sleep(1)
for g in range(0, pgt):
    jogos.append([])
    for r in range(0, 6):
        num = randint(1, 60)
        while num in jogos[g]:
            num = randint(1, 60)
        jogos[g].append(num)
    jogos[g].sort()
    print(f'\033[32;1mJogo {g+1}ª : {jogos[g]}\033[m')
    sleep(1)
