from random import randint
cont = 0
maior = 0
menor = 0
sor = (randint(0, 10),
       randint(0, 10),
       randint(0, 10),
       randint(0, 10),
       randint(0, 10),)
while cont < 5:
    if cont == 0:
        maior = menor = sor[cont]
    if sor[cont] > maior:
        maior = sor[cont]
    if sor[cont] < menor:
        menor = sor[cont]
    cont+=1
print(f'\033[35m{sor[:]}\033[m\n\033[34mO maior número é {maior}\033[m\n\033[31mO menor número é {menor}\033[m')


#ou sorteia já na tupla
#sort = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
#print(sort)
'''Para apresentar o maior da lista e a menor.'''
#print(max(sort), min(sort))