lista = []
par = []
inpar = []
while True:
    lista.append(int(input('\033[34mDigite um número:  ')))
    p = str(input('Deseja continuar:  \033[m'))
    if p in 'nNãÃoO':
        break
for r in range(0, len(lista)):
    if int(lista[r]) % 2 == 0:
        par.append(int(lista[r]))
    else:
        inpar.append(int(lista[r]))
print(f'\033[31mForam digitados {lista}')
lista = list(par)
print(f'Os pares digitados são {lista}')
lista = list(inpar)
print(f'Os inpares digitados foram {lista}\033[m')