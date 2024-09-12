
exp = list()
p = 0
c = 0
ch = 0
exp.append(str(input('\033[36mDigite a expressão:\033[m')))
print(exp)
print('\033[34m')
if '(' in exp[0]:
    p = exp.count('(') + exp.count(')')
    if p % 2 == 0:
        if exp.count('(') == exp[0].count(')'):
            print('Esta certo parenteses')
        else:
            print('\033[31m')
            print(exp[0].rfind(')')+1)
            print('Errado parenteses')
            print('\033[m')
    else:
        print('\033[31m')
        print('Errado parenteses')
        print('\033[m')
if '[' in exp[0]:
    c = exp.count('[') + exp.count(']')
    if c % 2 == 0:
        if exp[0].count('[') == exp[0].count(']'):
            print('Esta certo couchetes')
        else:
            print('\033[31m')
            print(exp[0].rfind(']') + 1)
            print('Errado couchetes')
            print('\033[m')
    else:
        print('\033[31m')
        print('Errado couchetes')
        print('\033[m')
if '{' in exp[0]:
    ch = exp.count('{') + exp.count('}')
    if ch % 2 == 0:
        if exp.count('{')== exp[0].count('}'):
            print('Esta certo chaves')
        else:
            print('\033[31m')
            print(exp[0].rfind('}') + 1)
            print('Errado chaves')
            print('\033[m')
    else:
        print('\033[31m')
        print('Errado chaves')
        print('\033[m')
print('\033[m')
if '{' in exp[0]:
    if '[' not in exp[0] and '(' not in exp[0]:
        print('\033[31m')
        print('Está errada a expressão')
        print('\033[m')
if'[' in exp[0]:
    if '(' not in exp[0]:
        print('\033[31m')
        print('Está errada a expressão')
        print('\033[m')