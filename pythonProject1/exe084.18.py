from time import sleep
ls = list(range(36, 9, -1))
print('\033[32m')
for s, n in enumerate(ls):
    print(f'Em {s} achei {n}')
    sleep(0.5)
print('Fim.\033[m')
lista = list(range(0, 20))
listaw = []
lista.append(1)
lista.count(2)
lista.sort()
lista.pop()




lista.insert(3, 10)
lista.reverse()
lista.remove(13)
del lista[7]
lista2 = lista[:]
lista3 = list(range(20, 0, -1))
dados = []
pessoas = []
nome = ''
idade = 0
cnt = 0
while True:
    nome = str(input('Nome:  '))
    idade = int(input('Idade:  '))
    dados.append(nome)
    dados.append(idade)
    pessoas.append(dados[:])
    dados.clear()
    cnt += 1
    if cnt == 3:
        break
ttmai = 0
ttmen = 0
for a in pessoas:
    if a[1]  >= 16:
        ttmai+=1
    else:
        ttmen+=1
print(f'{ttmai} pessoas podem tirar titulo de eleito. {ttmen}  pessoas não podem tirar o titulo de eleitor.')
print(pessoas)
print(pessoas[0])
print(pessoas[1])
print(pessoas[2])
print(pessoas[2][1])
print(pessoas[1][0])
usuarios = []
usuarios.append(pessoas[:])
print(usuarios[0][1][0])
for x in pessoas:
    print(x[1])
for z in pessoas:
    print(z[0])
for w in pessoas:
    print(f'\033[31m O aluno {w[0]} tem {w[1]} anos de idade.\033[m')