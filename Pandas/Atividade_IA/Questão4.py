import pandas as pd#bibliteca
import seaborn
titanic = pd.read_csv("titanic/titanic.csv")#caminho do arquivo no mesmo diretório
titan = pd.DataFrame(titanic)#transforma para dataframe



#4ª Questão:
'''4. Normalização/Padronização:
o Normalize ou padronize as colunas numéricas, como Age e Fare, usando a 
técnica adequada. Escolha entre normalização (Min-Max) ou 
padronização (Z-score) e justifique a escolha.'''

print(titan["Age"])
print(titan["Fare"])

id_tarifa = titan[["Age","Fare"]]#crio uma tablea com as duas colunas que vou manipular
print(id_tarifa)#antes
#Normalização da tabela com a formula abaixo
id_trf_padronizada = (id_tarifa - id_tarifa.mean())/id_tarifa.std()
print(id_trf_padronizada)#depois

print(f"\033[32m"
      f" Justificativa: Utilizeri padronização Z-score porque os dados são medias diferêntes nas duas\n"
      f"colunas manipuladas. Calcular desvio padrão é mais preciso quando se deseja visualizar dados distribuídos\n"
      f". É util para manipulação por IA, pois se adequa a regressão linear e análise de componentes principais.\n"
      f"\033[m")

