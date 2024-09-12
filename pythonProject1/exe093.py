n = str(input('Qual seu nome?  ')).strip().capitalize()
qp = int(input(f'Quantas partidas você jogou {n} ?  '))
lista = []
totg = 0
for g in range(0, qp):
    lista.append(int(input(f'Quantos gols você fez na {g+1}ª partida?  ')))
    totg += lista[g]
dic = {'Nome': n, 'Gols': lista, 'Total de gols': totg}
print('-='*50, '\n', dic, '\n', '-='*50)
for k, v in dic.items():
    print(f'No campo {k} tem o valor {v}.')
print('-='*50)
print(f'O jogador {dic["Nome"]} jogou {qp} partidas.')
for x in range(0, qp):
    print(f'    =>Na partida {x+1}ª você fez {dic["Gols"][x]} gols')
print('-='*50,f'\nFoi um total de {dic["Total de gols"]} gols')


