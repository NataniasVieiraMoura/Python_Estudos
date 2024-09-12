from time import sleep
from exe115.lib.interface import *



def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')



def lerArquivo(nome):
    import
    try:
        a.open(nome, 'wt')
        a.close()
    except:
        print(f'Houve um erro na criação do arquivo.')
    else:
        cabeçalho('pessoas cadastradas')
        print(a.readlines())