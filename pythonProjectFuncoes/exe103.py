

def ficha(gols,nome):
    """

    :param gols: Número de gols(se enter for digitado
    o resultado é 0)
    :param nome: Nome do jogador(se enter for digitado
    o resultado é <desconhecido>
    :return: um print(f'...{nome}...{gols}...')
    """
    if gols.isalpha():
        gols = 0
    if len(str(gols)) == 0:
        gols = 0
    if nome.isnumeric():
        nome = '<desconhecido>'
    else:
        gols = int(gols)
    if len(nome) == 0:
        nome = '<desconhecido>'
    return print(f'O jogador {nome} fez {gols} no campeonato.')


print('-'*35)
nome = str(input('Qual teu nome ?'))
gols = str(input('Quantos gols fez ?'))


ficha(gols, nome)