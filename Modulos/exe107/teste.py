

import moeda
p = float(input('Digite um preço'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobrar(p)}')
print(f'Almento de {p} em 80% é {moeda.almentar(p,80,True)}')
print(f'Diminuir de {p} em 20% é {moeda.diminuir(p,20)}')
