
def almentar(num=0,quant=0,ope=True):
    """

    :param num: numero que vai ser calculado
    :param quant: quantidade de soma ou produto
    :param ope: operação que vai ser efetuada(padronizado na soma como True)
    :return: escrever resultado res
    """
    res = 0
    if ope == True:
        res = num + (num*(quant/100))
        return res


def diminuir(num=0, quant=0):
    res = (num)-(num*(quant/100))
    return res



def dobrar(num=0, quant=2):
    res = (num)*quant
    return res



def metade(num=0,quant=2):
    res = (num)/quant
    return res


def moeda(txt, porta=True):
    """

    :param txt: texto que será formatado para receber R$
    :param porta: para caso não queira acrecentar R$
    :return: número formata com ou sem sifrão(padronizado True para com sifrão)
    """
    if porta:
        #x = f'R$ {txt}'
        x = str(txt)
        if '.' in x:
            x = x.replace('.', ',')
        x = f'R$ {x}'
        return x
    else:
        x = f'R$ {txt}'
        return x


def resumo(p=0, almento=0,d=0):
    x = 'RESUMO DO VALOR'
    print('-'*int(len(x)*2), '\n', ' '*int(len(x)/2), x)
    print('-'*int(len(x)*2))
    print(f'Preço analizado: \t {moeda(p)}')
    print(f'Dobro do preço: \t {moeda(dobrar(p))}')
    print(f'Metade do preço: \t {moeda(metade(p))}')
    print(f'80% de almento: \t {moeda(almentar(p,almento))}')
    print(f'35% de diminuição: \t {moeda(diminuir(p,d))}')
    print('-' * int(len(x) * 2))


