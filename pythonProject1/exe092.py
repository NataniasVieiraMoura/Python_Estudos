nome = str(input('Qual seu nome? '))
dnc = int(input(f'Qual ano {nome} naceu? '))
cdt = int(input(f'Número de contribuição(não possui? => digite 0):  '))
from datetime import date
ano = date.today().year
idade = ano - dnc
tds = 35
apos = 0
adc = 0
dic = {'Nome': nome, 'Idade': idade, 'Carteira T.': cdt}
if cdt != 0:
    adc = int(input('Digite o ano de sua contratação: '))
    apos = ano - adc
    sal = float(input('Digite seu salário: R$'))
    dic['Ano contratação'] = adc
    dic['Salário : R$'] = sal
    dic['Tempo de contribição'] = apos
apos = tds - apos
if dic['Carteira T.'] != 0:
    if apos > 0:
        dic['Aposentadoria'] = f'Você necessita contribuir {apos} anos.\nVocê se aposentará com {apos + dic["Idade"]} anos'
    if apos < 0:
        dic['Aposentadoria'] = f'Você já contribuiu {apos} anos. Aposentado'
    if apos == 0:
        dic['Aposentadoria'] = f'Você contribuiu o necessário. Parabéns aposentado'
for k, v in dic.items():
    print(f'Sr(a) {nome}, seu {k} é {v}.')