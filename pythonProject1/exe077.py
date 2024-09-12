palavras = ('Trabalho', 'Vogais', 'Terminal',
            'Maca', 'Corrida', 'Ventilador',
            'Caminho', 'Azuleijo', 'Tostadeira',
            'Adega','Forma', 'Treinamento',
            'Balistica', 'Acabe', 'Esmeralda',
            'Iris', 'Ouro', 'Urubu')
cnt1 = 0
a = e = i = o = u = 0
while cnt1 < len(palavras):
#   print(palavras[cnt1].lower())
    if 'a' in str(palavras[cnt1]).lower():
        a = str(palavras[cnt1]).lower().count('a')
    cnt2 = 0
    if 'e' in str(palavras[cnt1]).lower():
        e = str(palavras[cnt1]).lower().count('e')
    cnt2 = 0
    if 'i' in str(palavras[cnt1]).lower():
        i = str(palavras[cnt1]).lower().count('i')
    cnt2 = 0
    if 'o' in str(palavras[cnt1]).lower():
        o = str(palavras[cnt1]).lower().count('o')
    cnt2 = 0
    if 'u' in str(palavras[cnt1]).lower():
        u = str(palavras[cnt1]).lower().count('u')
    cnt2 = 0
    print(f'\033[34;1mA palavra {palavras[cnt1]} temos :\033[m', end='\033[33m')
    if a >= 1:
        print('a '*a, end='')
    if e >= 1:
        print('e '*e, end='')
    if i >= 1:
        print('i '*i, end='')
    if o >= 1:
        print('o '*o, end='')
    if u >= 1:
        print('u '*u, end='')
    print('\n', end='')
    cnt1 += 1
    a = e = i = o = u = 0
print('Fim\033[m')
