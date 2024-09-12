

def manual():
        """


        para parar o programa digite fim.
        foub : recebe uma função o biblioteca que
        vai para um help(foub)
        manual() <- executa a definição
        :return: nada
        """
        x = '  Sistema de Ajuda: Pyhelp'
        while True:
            print('\033[42m~~' + '~' * int(len(x)) + '~~')
            print(x)
            print('~~' + '~' * int(len(x))+ '~~', '\n\033[m', end='')

            foub = str(input('Função ou biblioteca> '))
            y = f'  Acessando o manual do {foub}'
            if foub.strip().lower()[0:3] == 'fim':
                a = 'Até logo!'
                print(f'\033[41m{"~"*int(len(a))}\n{a}\n',end=f'\n{"~"*int(len(a))}\n\033[m')
                break
            print('\033[46m~~'+'~'* int(len(y)) + '~~')
            print(y)
            print('~~' + '~' * int(len(y)) + '~~\n\033[m\033[7m',end='')
            print(help(foub), '\n\033[m',end='')


manual()