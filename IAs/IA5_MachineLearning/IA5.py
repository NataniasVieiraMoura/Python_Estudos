'''O mercado vai CAIR ou SUBIR? Machine Learning na prática!'''
'''Parei na aula 27 do curso de python para machine learning
    Continuar no minuto: 24:47
    Fazer todo o código abaixo no Colaboratório(jupter notebook) e continuar o vídeo'''
import pandas as pd
'''Exemplo de previsão das ações com machine learning'''
dataf = pd.read_csv("C:/Users/Natanael V. de Sousa/OneDrive/Área de Trabalho/Programas/Análise de Dados/Arquivo_csv/Arquivo(1)/GSPC.csv")
#print(dataf.head())
dataf = dataf.drop("Date",axis=1)#axis 1 é coluna,no caso Date
#print(dataf[-2::])#aqui você está pedindo para ver o final da tabela, no caso as duas última

amanha = dataf[-1::]#variavel recebe o ultimi elemento da tabela: 17.217
#print(amanha)

base = dataf.drop(dataf[-1::].index,axis=0)#axis 0 é linha, no caso dataf[-1::].index
#veja que tabela base recebe a tabela dataf sem  a linha 17.217
#print(base.tail())#esse método retorna as últimas 5 linhas

base["Target"] = base["Close"][1:len(base)].reset_index(drop=True)
'''Na linha 15 a coluna criada targuet recebe os dados da coluna Close
pulando a primeira linha(0) e comçando a partir da (1)'''
'''Logo o último registro será NaN pois foi removido o primeiro'''
#print(base.tail())

prev = base[-1::].drop("Target",axis=1)#armazena na váriável o útimo registro
#drop removeu o dado da tabela "Target"
#print(prev)

treino = base.drop(base[-1::].index,axis=0)
'''Treino recebe a tabela sem a última linha'''
#print(treino.tail())#no caso a linha 17.216

treino.loc[treino["Target"] > treino["Close"],"Target"] = 1
'''linha 30: toda vez que o valor de target for maior que o de close,
    o valor de target recebe 1'''
#print(treino.tail())

treino.loc[treino["Target"]!=1,"Target"] = 0
#print(treino.tail())

y = treino["Target"]#variavel de treino
x = treino.drop("Target", axis=1)#variável de treino

from sklearn.model_selection import train_test_split
x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size=0.3)
'''Linha 42: test_size define a quantidade 
do processamento total alocada para teste. Logo 70% será usada para treinar.
Linha 42: variáveis de treino e teste com o método train_teste_split
'''
from sklearn.ensemble import ExtraTreesClassifier
modelo = ExtraTreesClassifier()#objeto da ia para classificação
modelo.fit(x_treino,y_treino)#método de treino

resultado = modelo.score(x_teste,y_teste)
resultado = resultado*100
#variável recebe o resultado com
print(f"Acurácia: {resultado:.2f}%")#retorna em decimal  a porcentagem

print(prev)
print(modelo.predict(prev))#usa o modelo para fazer uma previsão
#linha 57: se o retorno for array[1.], quer dizer que o valor é maior
#linha 57: se o retorno for array[0.], quer dizer que o valor é menor

#print(amanha)
#base = base.append(amanha,sort=True)#Esse é executado no Colaboratório
#print(base.tail())

#prev.to_csv("C:/Prev.csv",index=False)#Esse é executado no Colaboratório
