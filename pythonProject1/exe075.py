listas = ((int(input('Digite um número:  '))),
          (int(input('Digite um outro:  '))),
          (int(input('Digite mais outro:  '))),
          (int(input('Digite um último número:  '))))
cnt9 = listas.count(9)
print(f'Você digitou {cnt9} vezes o número 9')
if 3 in listas:
    pos3 = listas.index(3)
    print('Você digiou o 3 na ', pos3 + 1, 'ª posição')
cnt = 0
cnt1 = 0
while cnt < 4:
    if listas[cnt] % 2 == 0:
        cnt1 += 1
        if cnt == 0:
            print('Os pares digitados são:', end=' ')
        print('---', listas[cnt], end='')
    cnt += 1
if cnt1 > 0:
    print('\n', end='')
    print(f'Você digiou {cnt1} números pares')
