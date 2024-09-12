'''Dicionário:  {} '''
'''Variáveis compostas: {}'''
dicn = dict()
lis = {'nome': 'pedro', 'idade': 25}
print(lis['nome'])
print(lis['idade'])
lis['sexo'] = 'Masculino'
del lis['idade']
filme = {'Titulo': 'Star Wars', 'Ano': '1977', 'Diretor': 'Jeorge Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())
for x, y in filme.items():
    print(f'O {x} é {y}')
animal = {'Nome': 'Zebra', 'Idade': 32, 'Sexo': 'Feminino'}
print(f'{animal["Nome"]} tem {animal["Idade"]}')
print(animal.keys())
print(animal.values())
print(animal.items())
for k in animal.keys():
    print(k)
for v in animal.values():
    print(v)
del animal['Idade']
animal['Nome'] = 'Javali'
animal['Peso'] = '89.60kg'
for k, v in animal.items():
    print(f'Na chave {k} há o valor {v}')
nacoes = list()
pais1 = {'País': 'Alemanha', 'Capital': 'Berlin'}
pais2 = {'País': 'Estados Unidos', 'Capital': 'Washington'}
pais3 = {'País': 'Japão', 'Capital': 'Tóquio'}
nacoes.append(pais1)
nacoes.append(pais2)
nacoes.append(pais3)
print(nacoes)
print(nacoes[2]['Capital'])
print(nacoes[1]['País'])
brasil = list()
estado = dict()
for t in range(0, 4):
    estado['Uf'] = str(input('Qual a unidade Federativa: '))
    estado['Sigla'] = str(input(f'Qual a sigla de {estado["Uf"]}? '))
    brasil.append(estado.copy())
for s in brasil:
    for d in s.values():
        print(d, end='-')
        print()
'''Eu posso criar bibliotecas sem declarar dicionários antes,
os dicionários já são as posições da lista, basta cria chaves em listas.'''
lista = [{'Nome': 'Gabriel' ,'Idade': 23}, {'Nome':'Rogerio','Idade': 58}, {'Nome':'Heitor','Idade': 21}, {'Nome':'Glauco','Idade': 54}]
print(lista[2]['Nome'])
print(lista[0].keys())
print(lista[1].values())
print(lista[2].items())
lista2 = ['Lista 2',{},{},{},{},{}]
print(lista2)
lista3 = ['Lista 3']
lista3.append({})
lista3.append([])
print(lista3)
lista4 = ['Lista 4']
lista4.append(list())
lista4.append(dict())
print(lista4)
'''Eu posso adicionar listas em dicionários e listas em listas em dicionários'''
dic = {'Cadastro':['Maria', '38 Anos', 'Solteira'], 'Situação':['Contratada', 'Estagiária','Administrativo']}
print(dic)
print(dic.values())
print(dic.keys())
print(dic.items())
print(dic['Cadastro'][1])
dic0 = {10.3:['Maria','Casada', '3 Filhos', 'Um pet'], 21:['João', 'Solteiro', '12 Anos', ['Não alistado', 'Sem titulo eleitoral']]}
print(dic0)
print(dic0.values())
print(dic0.keys())
print(dic0.items())
print(dic0[10.3][2])
print(dic0[21][3][0])
dic10 = {'Cadastro':[{'Nomes':{}}]}
print(dic10)