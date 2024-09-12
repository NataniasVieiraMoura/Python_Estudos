lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Conpasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 32.30,
         'Livro', 34.90)
for iten in range(0, len(lista)):
    if iten % 2 == 0:
        print(f'{lista[iten]:.<30}', end='')
    if iten % 2 == 1:
        print(f'R${lista[iten]:>8.2f}')
