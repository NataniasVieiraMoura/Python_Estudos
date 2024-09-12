'''Exercicio 78:'''
lista = []
pos = []
pos2 = []
lista2 = []
lista = []
for l in range(0, 5):
    lista.append(int(input(f'\033[34mDigite um número para a posição {l}:\033[m')))
lista2 = lista[:]
lista2.sort()
for k in range(0, 5):
    if lista[k] == lista2[0]:
        pos2.append(k+1)
    if lista[k] == lista2[4]:
        pos.append(k+1)
print(f'\033[32mVocê digitou {lista}')
print(f'O maior número é {lista2[4]} nas{pos}ª posições.')
print(f'O menor número é {lista2[0]} nas {pos2}ª posições.\033[m')
