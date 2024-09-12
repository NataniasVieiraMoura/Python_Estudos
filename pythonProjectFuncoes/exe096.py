print('  Controle de Terrenos')
print('-'*30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))


def area(l, c):
    r = l * c
    print(f'A area de seu terreno de {l}x{c} é de {r}m².')


area(l, c)
