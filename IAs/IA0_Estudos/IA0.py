'''Continuação apartir da aula 13 do curso python da playlist'''
#Configurações => ctrl + shift + s
#Fechar abas => ctrl + shift + f12
#Rum => alt + 4
#Recarregar => ctrl + f5
#Sair => shift + esc(scape)
#Ctrl + f11 => adicionar bookmark
#Feclar arquivo python => Ctrl + f4
def exibe(texto):
    print(f"\033[7m\n\033[m{texto}")
def b():
    print("\033[7m\n\033[m")
def destaq(texto):
    print(f"\033[40;33m{texto:_^100}\033[m")
import pandas as pd
alunosDc = {
    "Nomes": ["Maria","Eduarda","Camilla", "Alicíia","Camilla","Adelina","Eduarda","Camilla","Roberta","Adelina"],
    "Notas": [6,7,4,9,10,3,4,2,6,8],
    "Aprovados": ["não","sim","não","sim","sim","não","não","não","não","sim"]
}
tab_alDC = pd.DataFrame(alunosDc)
print(tab_alDC)
b()
#Filtros de linhas e colunas
print(tab_alDC["Nomes"])#Seleciona colunas
b()
print(tab_alDC["Notas"])
b()
print(tab_alDC["Aprovados"])
b()
print(tab_alDC.loc[[0,1,3]])#O método loc() recebe paramentro das linhas que você quer selecionar
b()
print(tab_alDC.loc[2:4])#O método retorna um intervalo de linhas
b()
print(tab_alDC.loc[tab_alDC["Nomes"]=="Eduarda"])#Rerna as linhas onde na coluna nomes for igual a "Eduarda"
exibe(tab_alDC.loc[tab_alDC["Nomes"]!="Camilla"])

'''Aula 15'''
'''Excluir linhas, manipular tabelas,...'''

pri_linhas = tab_alDC.loc[4:7]#seleciona um intervalo de linhas
exibe(pri_linhas)
média_al = tab_alDC.loc[tab_alDC["Notas"]== 6]
exibe(média_al)

esport = pd.read_csv("C:/Users/Natanael V. de Sousa/OneDrive/Área de Trabalho/Programas/Análise de Dados/athlete_events.csv")
exibe(esport.head())

'''Mudar o nome das colunas:'''
esport.rename(columns={"Name":"Sujeito","Event":"Esporte","Medal":"Medalha"}, inplace=True)
exibe(esport.head())

exibe(esport["Sujeito"])
dadosp = esport["Sujeito"]
exibe(type(dadosp))
exibe(esport["Medalha"].value_counts())#o método value_counts() mostra a ocorrencia
exibe(esport["City"].value_counts())
'''O método value_counts mostra quantas vezes um dado aparece'''
exibe(esport["Sex"].value_counts())
exibe(esport[:].describe())
'''Excluir uma coluna de uma DataFrame'''
'''Para excluir colunas utilize o método drop() com os parametros:
    Nome da coluna, "axis:0" para linha e "axis:1" para coluna, "inplace=True para continuar na mesma linha '''
esport.drop("Sex", axis=1, inplace=True)
esport.drop("Age",axis=1,inplace=True)
esport.drop("Height",axis=1,inplace=True)
esport.drop("Weight",axis=1,inplace=True)
esport.drop("NOC",axis=1,inplace=True)
esport.drop("Team",axis=1,inplace=True)
esport.drop("Games",axis=1,inplace=True)
esport.drop("Year",axis=1,inplace=True)
esport.drop("Season",axis=1,inplace=True)
esport.drop("City",axis=1,inplace=True)
exibe(esport.head(10))#veja que ele vai indicar que há apenas 5 colunas na tabela.
'''Parei na aula 17 do curso de ia com python'''