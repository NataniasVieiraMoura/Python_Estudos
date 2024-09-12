import pandas as pd
#Métodos do pandas
tabela = pd.read_csv("C:/Users/Natanael V. de Sousa/OneDrive/Área de Trabalho/Programas/Análise de Dados/athlete_events.csv")
cincol = tabela.head(5)
print(cincol)
def bar():
    print("\033[7m\n\033[m")
bar()
#Abaixo dicionário:
diciona = {"Cosecionária": ["Monte","Hesj","Galios","Fenando_SA","Tell_GRT"],"Notas": [7,5,4,2,9]
    ,"Aprovados": ["Não","Não","Não","Não","Sim"]}
print(diciona)
dataframe0 = pd.DataFrame(diciona)
tamanho_df = dataframe0.shape
bar()
descriçao = dataframe0.describe()
print(descriçao)
bar()
print(dataframe0["Cosecionária"],"\n",dataframe0["Notas"],"\n",dataframe0["Aprovados"])
bar()
