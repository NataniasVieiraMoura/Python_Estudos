


def notas(*l,sit=False):
    """

    :param l: Você pode inserir vários valores
    ou nenhum. Dá o total de notas, a maior, menor e a média
    :param sit:  Calcula a situacão do aluno
     se sit =True ele mostra, se sit, False ou não colocar,
     ele não informa
    :return: dicionário de notas dic{...}
    """
    cnt = 0
    lista = []
    sot = 0
    for x in l:
        cnt += 1
        lista.append(x)
        sot += x
    lista.sort()
    media = sot/cnt
    dic = {'Total de notas': cnt,'Maior': lista[cnt-1],'Menor': lista[0],'Média': media}
    if sit:
        if media == 7:
            dic['Situação'] = ' Boa'
        elif media < 7:
            dic['Situação'] = 'Ruim'
        elif media > 7:
            dic['Situação'] = 'Exelente'
    return dic



resp = notas(10,9.3,10,6.9,sit=True)
print(resp)
from time import sleep
sleep(1)


def n(*num, sit= False):
    """

    :param num: notas para análar
    :param sit: opcional true ou false
    ou nada  para informar o caso do aluno
    :return: dicionário dic com dados
    """
    dic = dict()
    dic['Total'] = len(num)
    dic['Maior'] = max(num)
    dic['Menor'] = min(num)
    dic['Média'] = sum(num)/len(num)
    if sit:
        if 3 < dic['Média'] <7:
            dic['Caso'] = 'Recuperação'
        if dic['Média'] < 3:
            dic['Caso'] = 'Reprovado'
        if dic['Média'] >7:
            dic['Caso'] = 'Aprovadissímo'
    return print(dic)

n(3, 10, 9, 4,5,10,2.6,4,7)

sleep(1)
help(n)
sleep(1)
help(notas)