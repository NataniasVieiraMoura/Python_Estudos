import pandas as pd
#bibliteca

#1ª Questão:
titanic = pd.read_csv("titanic/titanic.csv")#caminho do arquivo no mesmo diretório
#Estou utilizando conjunto de dados de um arquivo baixado
titan = pd.DataFrame(titanic)#transforma para dataframe
print(titan)

'''Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
      dtype='object')'''
#print(titanic.keys())





