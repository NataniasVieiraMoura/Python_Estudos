from moeda import moeda
from moeda import metade, dobrar, almentar, diminuir
p = float(input('Digite um preço'))
print(f'A metade de {p} é {moeda(metade(p), False)}')
print(f'O dobro de {moeda(p)} é {moeda(dobrar(p), True)}')
print(f'Almento de {moeda(p)} em 80% é {moeda(almentar(p,80,True), False)}')
print(f'Diminuir de {p} em 20% é {moeda(diminuir(p,20),True)}')


