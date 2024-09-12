lis = []
par = []
impar = []
lis.append(par)
lis.append(impar)
num = 0
for t in range(1, 8):
    num = int(input(f'{t}ª Número: '))
    if num % 2 == 0:
        par.insert(0, num)
    else:
        impar.insert(0, num)
par.sort()
impar.sort()
par.insert(0, 'Pares : ')
impar.insert(0, 'Impares : ')
print(f'\033[34mOs valores {lis[0]}\033[m\n\033[31mOs valores {lis[1]}\033[m')
