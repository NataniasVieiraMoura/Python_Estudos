l = list()
for q in range(0, 5):
    n = int(input('Digite um número: '))
    if q == 0 or n > l[-1]:
        l.append(n)
        print(f'O número {n} foi adicionado')
    else:
        port = 0
        while port < 5:
            if n <= l[port]:
                l.insert(port, n)
                print(f'Adicionado na posição {port}')
                break
            port += 1
print(f'Os numeros em ordem crecente ficam {l}')