matriz = [[], [], []]
num = sp = s3c = m2l = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'\033[34mDigite um número para a posição ({l},{c}) : \033[m'))
        matriz[l].append(num)
        if num % 2 == 0:
            sp += num
        if c == 2:
            s3c += num
        if l == 1:
            if num > m2l:
                m2l = num
for w in range(0, 3):
    print('\033[33;1m', matriz[w], '\033[m')
print(f'\033[34m A soma dos números pares é {sp}.\033[m')
print(f'\033[37m A soma dos números da 3ª coluna é {s3c}.\033[m')
print(f'\033[36m O maior número da 2ª linha é {m2l}.\033[m')
