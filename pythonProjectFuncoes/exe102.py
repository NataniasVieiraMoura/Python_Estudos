from time import sleep


def f(n,show=False):
    '\033[34m'"""
    ->Para calcular fatorial f(n,show = True)
    :param n: número para fatorar em um laço
    :param show: Bool para receber opção True ou False
    para permitir ver ou não um laço que demonstra o calculo
    :return: mostra ou não o processo antes do resultado.
    """'\033[m'
    rest = 1
    for q in range(n, 0, -1):
        rest *= q
    if show:
        for q in range(n, 0, -1):
            if q > 1:
                sleep(0.75)
                return print(f' {q} x ')
            else:
                sleep(0.75)
                return print(f'{q}')
        sleep(0.50)
        return print(f' = {rest}')
    else:
        sleep(0.5)
        return print(rest)


print('-'*35)
help(f)
f(4, False)

