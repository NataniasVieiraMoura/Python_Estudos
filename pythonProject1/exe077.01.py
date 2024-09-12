palavras = ('Trabalho', 'Vogais', 'Terminal',
            'Maca', 'Corrida', 'Ventilador',
            'Caminho', 'Azuleijo', 'Tostadeira',
            'Adega','Forma', 'Treinamento',
            'Balistica', 'Acabe', 'Esmeralda',
            'Iris', 'Ouro', 'Urubu')
for p in palavras:
    print(f'\033[37mNa palavra {p.upper()} temos: ', end='\033[m')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print('\033[31m', vogal, end='\033[m')
    print('\n', end='')