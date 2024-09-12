print('\033[32;4m{}Canpeonato Brasileiro de Futbol{}\033[m'.format('*'*10, '*'*10))
tior = ('Botafogo', 'Palmeras', 'Atlético-MG', 'Grêmio', 'Fluminense', 'Athletico-PR', 'São Paulo', 'Fortaleza', 'Flamengo', 'Cruzeiro', 'Bragantino', 'Santos', 'Internacional', 'Cuiabá', 'Bahia', 'Corinthians', 'Goiás', 'América-MG', 'Vasco Da Gama', 'Coritiba')
print('\033[37m', '_'*45, '\033[m')
print('\033[37m', tior[0:5], '\n', tior[5:11], '\n', tior[11:16], '\n', tior[16:], '\033[m')
print('\033[37m', '_'*45, '\033[m')
#No lugar da Chapecoense eu escolhi o São Paulo
print('\033[35m', '#'*45, '\033[m')
print(f'\033[33mOs times em Ordem alfabetica:\033[m')
print('\033[33m', sorted(tior), '\033[m')
print('\033[35m', '#'*45, '\033[m')
print(f'\033[35mOs 5 primeiros colocados são :\033[m\n\033[34m{tior[0:5]}\033[m')
print('\033[35m', '#'*45, '\033[m')
print(f'\033[35mOs últimos 4 colocados são :\033[m\n\033[31m{tior[16: 20]}\033[m')#ou tior[-4:]
print('\033[35m', '#'*45, '\033[m')
print(f'\033[36mO São Paulo se encontra na ', tior.index('São Paulo') + 1, 'ª posição\033[m')


#for x in tior:
#   print(x)

