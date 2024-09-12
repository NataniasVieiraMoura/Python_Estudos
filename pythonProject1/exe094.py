print('\033[37;7m')
from math import floor
l = []
mig = 0
lm = []
m = []
pim = []
c = 0
while True:
    n = str(input('Qual seu nome?  '))
    s = str(input(f'Qual seu sexo {n} ?  ')).strip().upper()[0]
    while s not in 'FM':
        s = str(input(f'Qual seu sexo {n} ?  ')).strip().upper()[0]
    i = int(input(f'Qual sua idade {n} ?  '))
    mig += i
    l.append({'Nome': n, 'Sexo': s, 'Idade': i})
    if l[c]['Sexo'] == 'F':
        lm.append(n)
    cnt = str(input('Deseja continuar?  ')).strip().lower()[0]
    while cnt not in 'sn':
        cnt = str(input('Deseja continuar?  ')).strip().lower()[0]
    if cnt == 'n':
        break
    c +=1
mig = mig/int(len(l))
mig = floor(mig)
for x in range(0, len(l)):
    if mig <= l[x]['Idade']:
        pim.append(l[x])
print(f'Foram cadastradas {len(l[:])} pessoas.\nA média de idade do grupo é {mig} anos')
print(f'As mulheres cadastradas foram:\n {lm}')
print(f'As pessoas acima da média total do grupo é: ')
for x in range(0, len(l)):
    if mig <= l[x]['Idade']:
        print(l[x],'\n')
print()
print('\033[m')