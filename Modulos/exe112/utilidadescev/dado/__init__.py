from exe111.utilidadescev import resumo


def leiadinheiro(x):
    from exe111.utilidadescev import resumo, moeda
    if x.isalpha():
        print(f'\033[31m O dado {x} não é número.\033[m')
    else:
        x = float(x)
        print('\033[34m')
        resumo(x, 10, 15)
        print('\033[m')
