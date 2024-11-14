import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns

# Carregar o dataset
titanic = pd.read_csv("titanic/titanic.csv")

# Transformar para DataFrame
titan = pd.DataFrame(titanic)

# Preencher valores NaN na coluna 'Survived' com 0
titan["Survived"].fillna(0, inplace=True)

# Criar variáveis dummy para a coluna 'Sex'
titan = pd.get_dummies(titan, columns=["Sex"], drop_first=True)

# Preencher valores NaN nas colunas especificadas com 0
titan["Age"].fillna(0, inplace=True)
titan["PassengerId"].fillna(0, inplace=True)

# Separar variáveis independentes X da variável dependente y
X = titan[['Pclass', 'Sex_male', 'Age']]
y = titan["Survived"]

# Dividir em treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Treinando o modelo
regressor = LogisticRegression()
regressor.fit(X_train, y_train)

#previsões
previsao = regressor.predict(X_test)

# Mostar previsões
print(f"E a predição dos dados é {previsao}")
