'''Pareina aula 24ª'''
'''Ctrl + f4 para fechar aba'''
'''Códigos com machine learning se dividem geralmente em duas partes:
    Uma para treinar o modelo e outra para testar o modelo'''
'''Faça esse código no jupter notebook'''
'''Bibliotecas: '''
import pandas as pd
dataset = pd.read_csv("C:/Users/Natanael V. de Sousa/OneDrive/Área de Trabalho/Programas/Nias/wine_dataset.csv")
#print(dataset.head())
'''Perceba que o dataset tem a última coluna com valores do tipo string, mas
    para poder utilizar a IA devemos atribuir valores númericos:
    No caso 1 para red e 0 para white.'''

dataset["style"] = dataset["style"].replace("red",1)
dataset["style"] = dataset["style"].replace("white",0)
#colunas = dataset.columns
#linhas = dataset.index
#print(f"Colunas:\n{colunas}\nLinhas:\n{linhas}")

'''Separa as variáveis em variáevis préditoras e variáveis alvo.'''
predtora = dataset["style"]#recebe a coluna style com os dados alvo
alvo = dataset.drop("style",axis=1)#recebe os dados que serão usados para prever os dados alvo
print(predtora,"\n",alvo)

'''Conjunto de treino:'''
#Biblioteca:
from sklearn.model_selection import train_test_split
#criando os conjuntos de dados de treino e de teste
'''Na linhas abaixo as variáveis de treino recebem 30% das linhas para a IA
treinar. E as variaveis de teste ficam com os 70%'''
predtora_treino, predtora_teste, alvo_treino, alvo_teste = train_test_split(predtora, alvo, test_size=0.3)

'''Conjunto de teste:'''
#Biblioteca:
from sklearn.ensemble import ExtraTreesClassifier
#Criação do modelo:
model = ExtraTreesClassifier()#variável recebe a função da IA de classificação
model.fit(predtora_treino,alvo_treino)#fit()aplica a função da IA usando como
#parametros as variáveis de treino

#imprimindo resutado:
resultado = model.score(predtora_teste,alvo_teste)#score() é uma função de porcentagem de acertos
print("Acurácia:", resultado)

previsão = modelo.predict(predtora_teste[400:403])
print(previsão)