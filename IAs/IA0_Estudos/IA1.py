
'''Continuando apartir da aula 18 do curso IA com python'''
#Criação de Histogramas: Gráficos de barras
import pandas as pd
tabela = pd.read_csv("C:/Users/Natanael V. de Sousa/OneDrive/Área de Trabalho/Programas/Análise de Dados/athlete_events.csv")
import matplotlib.pyplot as plt
'''Essa bibliteca serve para criar gráficos com os dados da tabela'''
#biblioteca de gráficos
#tabela.hist(column="Age",bins=20)
'''O método hist() é do pandas. Ele mostra quantas vezes determinados
    valores ocorreram. Têm parametros: 
    column => coluna que deseja utilizar;
    bins => qantidade de barras'''
#print(plt.show())
'''não terminei a aula 18 do curso. Continue apartir dela'''

#tabela.hist(column="Age", bins=100)
#print(plt.show())

#tabela.hist(column="Weight", bins=100)
#print(plt.show())

#tabela.hist(column="Height", bins=150)
#print(plt.show())

import numpy
array_ers = numpy.array([x/2 for x in range(1,11)])
#plt.hist(array_ers,bins=300)
#print(plt.show())

''''
Box plot
Percentil:
Quartil, Pertil, mediana...
º
º
º(pontos fora da curva normal)
|-Linha superior(LS)
|
[ ]-Quartil 3       }
|-Mediana           }AIQ
[ ]-Quartil 1       }
|
|-Linha inferior(LI)
º(ponto fora da curva normal)
º
º
Para calcular a linha superior(LS):
    LS = Q3 + 1.5(Q3-Q1)
    LI = Q1 - 1,5(Q3-Q1)
'''

'''Box Plot no python: Mostra a distribuição dos dados na tabela'''
#tabela = pd.read_csv("C:/Users/Natanael V. de Sousa/OneDrive/Área de Trabalho/Programas/Análise de Dados/athlete_events.csv")
#print(tabela.head(5))
#tabela.boxplot(column=["Age","Weight","Height"])#colunas escolhidas para análise
#print(plt.show())#mostrar o gráfico

'''Criando gráficos com o matplotlib:'''
#x = [dado for dado in range(1,21)]
#y = [dados for dados in range(1,21)]
#plt.scatter(x,y)
#print(plt.show())


#dadosk = numpy.arange(-1000,1000,1)#cria um array.
'''O método arange cria arrays:
    paramentros: inicio, fim, incremeto'''
#print(dadosk)
'''Função no matplotlib: o método plot aplica uma função ao gráfico.
    Para esse método os parametros são: array e o calculo que deve ocorrer com cada valor do array
    como no exemplo abaixo:'''
#plt.plot(dadosk, -dadosk**3+4)
#print(plt.show())

#Exercicio: mostrar na lista altura e peso dos atletas:
#tabela.boxplot(column=["Weight","Height"])

'''Dados de homens e mulheres'''
#peso = tabela["Weight"]
#altura = tabela["Height"]
#plt.scatter(peso,altura)
#print(plt.show())

'''Dados apenas de homens'''
#masc = tabela.loc[tabela["Sex"]=="M"]
#peso_masc = masc["Weight"]
#altura_masc = masc["Height"]
#plt.scatter(peso_masc,altura_masc)
#plt.show()

#colunas = tabela.columns
#print(colunas)

'''Como lidar com dados faltantes(NaN) em um dataframe'''
'''A função dropna() remove as linhas com células faltantes faltantes(NaN) da tabela'''
dados2 = tabela.dropna()
print(f"{tabela.shape}\n{dados2.shape}")
'''A função isnull() muda os valores das células para True se o dado for NaN e False se o dado
da célula for qualquer outro.'''
tal_tf_nan = tabela.isnull()
print(tal_tf_nan)
'''A função sum() soma a quantidade de dados True, ou seja, dados faltantes para cada coluna'''
quais_true = tabela.isnull().sum()
print(quais_true)

quais_true_perc = (tabela.isnull().sum() / len(tabela["ID"]))*100
print(quais_true_perc)


tabela["Medal"].fillna("-----",inplace=True)#esse comando é para jupter notebook
tabela["Age"].fillna(0,inplace=True)#comando para jupter notebook
tabela["Weight"].fillna("Nada",inplace=True)#comando para jupter notebook
tabela["Height"].fillna("Nada_Aqui",inplace=True)#comando para jupter notebook

#pd.set_option('display.max_columns', None)#para exibir todas as culunas
#pd.set_option('display.max_columns', None)
#print(tabela.head())

'''Abaixo como os dados NaN forma alterados o resultado será 0 para todas as
colunas.'''
quais_true_perc = (tabela.isnull().sum() / len(tabela["ID"]))*100
print(quais_true_perc)
