
def almentar(num=0,quant=0,ope=True):
    """

    :param num: numero que vai ser calculado
    :param quant: quantidade de soma ou produto
    :param ope: operação que vai ser efetuada(padronizado na soma como True)
    :return: escrever resultado res
    """
    res = 0
    if ope == True:
        res = num + quant
    elif ope == False:
        res = (num) * quant
    elif False != ope != True:
        res = num + quant
    return res


def diminuir(num=0, quant=0):
    res = (num)-quant
    return res



def dobrar(num=0, quant=2):
    res = (num)*quant
    return res



def metade(num=0,quant=2):
    from math import floor
    res = (num)/quant
    res = floor(res)
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
        x = f'{txt}'
        return x

