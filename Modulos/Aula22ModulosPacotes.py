'''Modularização (1960, sistemas maiores, divide um programa em modulos
foco na legibilidade e facilitar a manutenção)'''
'''Vantagems:
Organização
facilidade de manutenção
Ocultação do codigo detalhado
Reutilizar em outros projetos
'''

'''Pacotes: Pasta com modulos(Bibliotecas)'''


from FunPersonalizadas import numeros
dados = int(input('Digite um número:'))
print(f'O fatorial de {dados} é {numeros.fat(dados)}')
print(f'O dobro de {dados} é {numeros.dobro(dados)}')
print(f'O triplo de {dados} é {numeros.triplo(dados)}')
