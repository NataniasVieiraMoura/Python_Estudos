dic = {}
lista = []
gols = []
totg = 0
cod = 0
while True:
    print('-'*50)
    dic['Nome'] = str(input('Digite seu nome: '))
    qp = int(input(f'Digite quantas partidas jogou {dic["Nome"]}?'))
    for g in range(0, qp):
        gols.append(int(input(f'Quantos gols  você fez na {g+1}ª partida?')))
        totg += int(gols[g])
    dic['Gols'] = gols[:]
    dic['Total'] = totg
    lista.append(dic.copy())
    gols.clear()
    dic.clear()
    cod += 1
    totg = 0
    cnt = str(input('Deseja continuar(s/n)?')).strip().lower()[0]
    while cnt not in 'sn':
        cnt = str(input('Erro ao digitar(responda S ou N).Deseja continuar(s/n)?')).strip().lower()[0]
    if cnt[0] == 'n':
        break
print('-='*50)
print('{: >4} {: <15}{: <16}{: <17}'.format('Cod', 'Nome', 'Gols', 'Total'))
d = 0
for x in lista:
    print(f'{d: >4} ', end='')
    for v in x.values():
        print(f'{str(v): <15}', end='')
    print('\n')
    d += 1
while True:
    print('-'*30)
    dados = int(input('Mostrar qual jogador?(Encerrar=>999) '))
    if dados != 999:
        if dados >= int(len(lista)):
            print(f'\033[31;1m Erro. O codigo {dados} não existe. Tente novamente. \033[m')
        if dados < len(lista):
            for x in range(0, int(len(lista[dados]['Gols'][:]))):
                print(f'No {x+1}ª jogo, {lista[dados]["Nome"]} fez {lista[dados]["Gols"][x]}')
    if dados == 999:
        break
print('<<Volte sempre>>')
