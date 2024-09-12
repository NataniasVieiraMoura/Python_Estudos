
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


def diminuir(num, quant):
    res = (num)-quant
    return res



def dobrar(num, quant=2):
    res = (num)*quant
    return res



def metade(num,quant=2):
    from math import floor
    res = (num)/quant
    res = floor(res)
    return res


def calculador(num=0, quant=0,ope=str):
    if ope == '*':
        return almentar(num, quant, ope=False)
    if ope == '+':
        return almentar(num, quant,)
    if ope == '*2':
        return dobrar(num,quant)
    if ope == '/2':
        return metade(num, quant)
    if ope == '-':
        return diminuir(num, quant)
    if ope == '/':
        from math import floor
        return print(floor(num/quant))