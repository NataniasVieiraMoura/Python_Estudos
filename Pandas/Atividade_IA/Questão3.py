import pandas as pd#bibliteca

import seaborn
titanic = pd.read_csv("titanic/titanic.csv")#caminho do arquivo no mesmo diretório
titan = pd.DataFrame(titanic)#transforma para dataframe

# 3ª Questão :
'''3. Transformação de Dados:
o 3.1. Converta a variável categórica Sex em variáveis numéricas (ex: Male = 1, 
Female = 0).'''
#parte 1 da 3ªQuestão:
print(titan["Sex"])#ver coluna
titan["Sex"].replace("male",1,inplace=True)#homem é 1 e mulher é 0
titan["Sex"].replace("female",0,inplace=True)
print(titan["Sex"])#veja como fica a coluna após alteração

print("\033[7m\n\033[m")

'''o 3.2. Converta a variável categórica Embarked em variáveis numéricas 
utilizando a técnica One-Hot Encoding (utilize pd.get_dummies).'''

print(titan["Embarked"])#antes
tab_col_bi = pd.get_dummies(titan,columns=["Embarked"])#especifique o dataframe e a coluna
'''Cria novas colunas detalhando a frequencia e quais valores aparecem em cada registro da coluna'''
print(tab_col_bi)#depois


