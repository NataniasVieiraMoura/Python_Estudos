dic = {}
dic['Aluno'] = str(input('Digite seu nome:  ')).strip().title()
dic['Média'] = float(input(f'Qual sua média {dic["Aluno"]}? '))
if dic['Média'] >= 7:
    dic['Situação'] = 'Aprovado'
elif 5 <= dic['Média'] < 7:
    dic['Situação'] = 'Recuperação'
else:
    dic['Situação'] = 'Reprovado'
print('-='*25)
for k, v in dic.items():
    print(f'{k} é igual a {v}')
