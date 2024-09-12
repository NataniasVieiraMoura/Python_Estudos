'''Biblioteca NumPy'''
'''Operações com matrizes e votores'''
import numpy as n
'''Construção de um array abaixo:'''
ar = n.array([1,2,3])
#O "as n" no import numpy e uma função para apelidar a biliboteca
print(ar)
print(type(ar))

ar3d = n.array([(0,1,2),(3,4,5),(6,7,8)])#cria uma matriz, onde cada parentesis é uma linha
print(ar3d)

print(n.max(ar3d))#maior elemento do array
print(n.min(ar3d))#menor elemento do array
print(n.mean(ar3d))#media dos elementos do array
print(n.std(ar3d))#desvio padrão dos elementos do array
'''Criação rapda de matriz:'''
ar_zeros = n.zeros((4,3))
'''O método zeros() do numpy cria uma matriz com as dimensões, respectivamente linha/coluna'''
print(ar_zeros)

ar_uns = n.ones((3,19))
'''O método ones() segue o raciocínio do zeros()'''
print(ar_uns)

ar_x = n.eye(5)#o método eye() cria uma matriz com linhas e colunas iguais
print(ar_x)

'''Biblioteca Pandas'''
'''Essa biblioteca é voltada para manipulação de dataframes ou tabelas com linhas e colunas'''
import pandas as pd
'''Abaixo: uma variável recebe o método "read_excel()" que vai ler o documento excel;
    Nesse método coloque o caminho do arquivo(organize: as barra devem estar para a direita);
     Acrecente ao final do "caminho do arquivo" outra barra e o nome do arquivo xlsx(a tabela 
      do excel) que deseja utilizar;'''
tabela = pd.read_excel('C:/Users/Natanael V. de Sousa/OneDrive/Área de Trabalho/Programas/Análise de Dados/IA(Chat_GPT).xlsx')

print(tabela.head())#head é um método de leitura do pandas
'''O método head() mostra as primeiras 5 linhas por padrão. Você pode pedir mais entre parentesis'''
print(tabela.head(7))

'''Abaixo: Abrindo arquivos .csv'''

tab_csv = pd.read_csv("C:/Users/Natanael V. de Sousa/OneDrive/Área de Trabalho/Programas/Análise de Dados/athlete_events.csv")
print(tab_csv.head(5))

comp_res = {"Cosecionária": ["Monte","Hesj","Galios","Fenando_SA","Tell_GRT"],"Notas": [7,5,4,2,9]
    ,"Aprovados": ["Não","Não","Não","Não","Sim"]}
#Abaixo a biblioteca comp_res vai ser inserida como tabela na variável dataframe_0
dataframe_0 = pd.DataFrame(comp_res)#transformei a variável dataframe_0 em um dataframe
print(dataframe_0)

objeto0 = pd.Series([2,3,5,6,4])#cria vetores unidimensionais com indices
print(objeto0)

array_3d = n.array([(6,3,8,9,5),(7,32,65,98,1)])
print(array_3d)

array1 = n.array([86,37,28,94,35])#array pode ser multidimensional
array1 = pd.Series(array1)#Método da biblioteca array
print(array1)
'''Não é possivel utilizar Series() em arrays de mais de uma dimensão'''

print(dataframe_0.head())
print(dataframe_0.shape)
#Método para receber o tamanh da tabela(linhasXcolunas), geralmente sem pararentesis
print(dataframe_0.describe())
'''O método describe() retorna os seguintes dados:
count => quantos dados
mean => média aritmética
std => desvio padrão dos dados
min => valor mímino
percentil 25%
percentil 50%
percentil 75%
max => valor máximo'''

def barrab():
    print("\033[7m\n\033[m")
barrab()
print(dataframe_0)
barrab()
print(dataframe_0["Cosecionária"])
barrab()
print(dataframe_0["Notas"])
barrab()

