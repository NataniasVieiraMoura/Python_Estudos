tpx = ('Feijão', 13.34, 'Arroz', 19.27, 'Queijo', 32.12, 'Margarina', 5.76, 'Macarão', 10.45, 'Azeite de Oliva', 21.31, 'Requeijão', 2.73, 'Farinha', 13.14, 'Ovo', 5.00, 'Leite', 5.50)
print(f'\033[32m', '-'*50, '\033[m')
print('\033[32m {:^50}\033[M'.format('Lista de Preços'))
print(f'\033[32m', '-'*50, '\033[m')
contador = contador2 = passo = p = cont = maior = pi = par = 0
cont4 = 0
m = 1
while cont < 10:
    if len(tpx[p]) > maior:
        maior = len(tpx[p])
    p += 2
    cont += 1
p = 0
while len(tpx) > passo:
    if passo % 2 == 0:
        print(f'\033[33m{tpx[passo]:.<30}\033[m', end='')
    if passo % 2 == 1:
        print(f'\033[34mR${tpx[passo]:>8.2f}\033[m')
    passo += 1
print(f'\033[32m', '-'*45, ' \033[m')