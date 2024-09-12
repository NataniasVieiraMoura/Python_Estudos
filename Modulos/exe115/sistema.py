from time import sleep
from exe115.lib.interface import *
from arquivo import *
arq = 'cursoemvideo.txt'
if arqExiste(arq):
    print('Sim')
else:
    print('Não')
if not arqExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(lista=['Criar Arquivo', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(nome)
    elif resposta == 2:
        cabeçalho('')
    elif resposta == 3:
        cabeçalho('Saindo do sistema')
        for x in range(0, 5):
            sleep(0.55)
            print('.', end='')
        print('\nAté logo.')
        break
    else:
        print('\033[31mErro. Digite uma opção válida.\033[m')
    sleep(0.5)
