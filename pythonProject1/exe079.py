lista = []
while True:
    lista.append(int(input('\033[34mDigite números:\033[m')))
    if lista.count(lista[int(len(lista)) - 1]) > 1:
        lista.pop()
        print('\033[31mVocê não pode repetir números cadastrados.\033[m')
    contin = str(input('\033[36mContinuar [Sim/Não] :\033[m'))
    if contin not in 'sSiImM':
        break
lista.sort()
print(f'\033[35mOs números cadastrados foram {lista}')
print('Fim\033[m')