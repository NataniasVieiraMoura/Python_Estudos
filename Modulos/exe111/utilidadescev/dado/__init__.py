

def leiadinheiro(x=str):
    if x.isdecimal:
        return print(f'Ok o valor : R$ {x} foi aceito.')
    else:
        return print(f'O dado {x} não foi aceito. Tenha um bom dia')
