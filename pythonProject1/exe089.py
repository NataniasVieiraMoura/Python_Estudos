from time import sleep
cdst = list()
notas = []
cnt = 0
while True:
    print('-='*45)
    nome = str(input('\033[32m Digite seu nome: '))
    sleep(0.75)
    not1 = float(input('Digite sua primeira nota: '))
    sleep(0.75)
    not2 = float(input('Digite sua segunda nota:\033[m'))
    cdst.append([])
    cdst[cnt].append(f'Aluno(a): {nome}')
    notas.append(f'1ª Nota: {not1}')
    notas.append(f'2ª Nota: {not2}')
    cdst[cnt].append(notas[:])
    notas.clear()
    cdst[cnt].append(f'Média: {(not1+not2)/2}')
    cnt += 1
    pgt = str(input('\033[33mDeseja continuar: \033[m')).lower().strip()
    if pgt[0] in 'n':
        break
print('\033[33mNu',' '*5,'Nome', ' '*4, 'Média\033[m')
for m in range(0, cnt):
    print('\033[33mNu', m, ' '*5, cdst[m][0], ' '*4, cdst[m][2], '\033[m')
porta = True
while True:
    porta = True
    sleep(1)
    p = str(input('\033[34;1mDeseja ver boletins? ')).strip().lower()
    if p[0] == 'n':
        break
    aluno = str(input('Qual aluno(a)?\033[m  '))
    sleep(0.5)
    for d in range(0, cnt):
        if aluno in cdst[d][0]:
            print('\033[37;1m.', end='')
            sleep(0.90)
            print('.', end='')
            sleep(0.60)
            print('.', end='')
            sleep(0.50)
            print(f'Achei o(a) {aluno}:')
            print(f'{cdst[d][1][:]}\033[m')
            porta = False
            break
    if porta == True:
        print(f'\033[31mO aluno(a) {aluno} não existe\033[m.')
print('Fim')



