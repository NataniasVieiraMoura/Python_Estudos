lista = []
lista2 = []
lista3 = []
cnt = 0
maior = 0
menor = 0
while True:
    cnt += 1
    nome = str(input('Digite seu nome:'))
    peso = float(input(f'Digite seu peso Sr(a) {nome} :'))
    c = str(input('Deseja continuar: ')).strip().lower()
    c = c[0]
    lista.append(peso)
    lista.append(nome)
    if cnt == 1:
        menor = maior = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
    if c in 'nN':
        break
for y, x in enumerate(lista):
    if x == maior:
        lista2.append(lista[y+1])
    if x == menor:
        lista3.append(lista[y+1])
print(f'Foram realizados {cnt} cadastros.')
print(f'O maior peso foi {maior} de {lista2}')
print(f'O menor peso foi {menor} de {lista3}')
print('Fim.')
