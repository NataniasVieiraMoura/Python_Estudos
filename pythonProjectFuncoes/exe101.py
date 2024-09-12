#from datetime import date
#print('-'*35)
#anonc = int(input('Digite seu ano de nacimento:  '))
#idade = date.today().year - anonc

def voto():
    from datetime import date
    print("-" * 35)
    anonc = int(input('Digite seu ano de nacimento:  '))
    idade = date.today().year - anonc

    situacao = f'Com {idade} anos : '
    if idade < 16:
        return situacao + f'Voto Negado\n{"-" * 35}'
    elif 17 == idade == 16:
        return situacao + f'Voto Facultativo\n{"-" * 35}'
    elif 18 <= idade <= 70:
        return situacao + f'Voto Obrigatório\n{"-" * 35}'
    elif idade > 70:
        return situacao + f'Voto Facultativo\n{"-" * 35}'


print(voto())

