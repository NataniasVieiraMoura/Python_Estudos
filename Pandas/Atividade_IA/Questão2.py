import pandas as pd#bibliteca
import seaborn
from sklearn.decomposition import non_negative_factorization

titanic = pd.read_csv("titanic/titanic.csv")#caminho do arquivo no mesmo diretório
titan = pd.DataFrame(titanic)#transforma para dataframe
#2ª Questão :

'''2. Limpeza de Dados:
o Verifique se há dados ausentes (missing data) e, se houver, trate esses 
valores:'''

'''▪ 2.1. Substitua valores ausentes na coluna Age pela média.'''
print(titan["Age"])#antes
media = float(titan["Age"].mean()).__ceil__()#ceil aredonda para mais. mean é função para média
titan["Age"].fillna(value=media,inplace=True)#altera valores NotANumber pelo valor atribuido em value
print(titan["Age"])#depois

print("\033[7m\n\033[m")

'''▪ 2.2. Substitua valores ausentes na coluna Embarked pelo valor mais 
comum (moda)'''
#print(titan["Embarked"].loc[:50])#você pode ver os registros completos com .loc de 50 em 50
#print(titan["Embarked"].loc[50:100])#aqui descobri que há NotANumber
#print(titan["Embarked"].loc[100:150])
#print(titan["Embarked"].loc[150:200])
#print(titan["Embarked"].loc[200:250])

pd.set_option("display.max_rows",None)#para ver todas as linhas de uma coluna do dataframe
#print(titan["Embarked"])#.set_option é melhor que ver de 50 em 50 regitros
#linhas NotANumber : 61 e 821
print(titan["Embarked"].loc[61])#descobri as linhas NaN
print(titan["Embarked"].loc[821])

valores = set(titan["Embarked"])#um set é uma lista não permite valores repetidos
print(valores)#veja
#{'Q', nan, 'C', 'S'}
ques = (titan["Embarked"] == "Q").sum()#quantos vezes aparece a string
nans = (titan["Embarked"] == "NaN").sum()
ces = (titan["Embarked"] == "C").sum()
eses = (titan["Embarked"] == "S").sum()
lista = [ques,nans, ces, eses]#lista dos resultados
moda = max(lista)#o que mais aparece é S
print(moda)#S é a moda

#Alteração de valores
titan["Embarked"].fillna(value="S",inplace=True)#trocar os NaN por um valor
titan["Embarked"].fillna(value="S",implace=True)

#resultado
print(titan["Embarked"].loc[61])#veja que o dataframe foi alterado
print(titan["Embarked"].loc[821])#cada valor NaN existente foi alterado para a moda
