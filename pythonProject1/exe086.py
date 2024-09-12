matriz = [[], [], []]
num = 0
for m in range(0, 3):
    if m == 0:
        for l in range(0, 3):
            for c in range(0, 3):
                num = float(input(f'\033[34mDigite um número para a posição ({l},{c}) : \033[m'))
                matriz[l].append(num)
    print(f'\033[33;1m {matriz[m]}\033[m')
