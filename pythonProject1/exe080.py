lista = [0,0,0,0,0]
cnt = 0
c = 0
porta = 1
while c < 5:
    numero = int(input('Digite :'))
    for d in range(0, 5):
        if numero > lista[d]:
            cnt+=1
    if cnt > 0:
        lista.insert(cnt, numero)
        print(lista)
        lista.pop(0)
        print(lista)
        porta = 0
    cnt = 0
    if porta != 0:
        for a in range(0, 5):
            if numero < lista[a]:
                cnt +=1
        if cnt > 0:
            lista.insert(cnt, numero)
            print(lista)
            lista.pop(0)
            print(lista)
    porta = 1
    c += 1
print('Fim')



'''Forma resumida do Exercicio abaixo:'''

lista = [0,0,0,0,0]
cnt = 0
c = 0
porta = 1
while c < 5:
    numero = int(input('Digite :'))
    for d in range(0, 5):
        if numero > lista[d]:
            cnt+=1
        porta = 0
        if porta != 0:
            for a in range(0, 5):
                if numero < lista[a]:
                    cnt += 1
    if cnt > 0:
        lista.insert(cnt, numero)
        print(lista)
        lista.pop(0)
        print(lista)
    cnt =0
    porta = 1
    c += 1
print('Fim')

