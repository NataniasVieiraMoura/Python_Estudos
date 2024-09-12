import numpy as np
import pandas as pd
matriz_bd = np.array([(15,32,96),(55,22,36)])
matriz_tri = np.array([(2,6,98),(4,75,61),(91,20,13)])
carac_mbd = np.array([(matriz_bd.max(),matriz_bd.min(), matriz_bd.std()),
                      (matriz_tri.max(),matriz_tri.min(), matriz_tri.std())])
print(f"{matriz_bd}\n{matriz_tri}\n{carac_mbd}")

tabela = pd.read_excel('C:/Users/Natanael V. de Sousa/OneDrive/Área de Trabalho/Programas/Análise de Dados/Tabelas/Importação.xlsx')
print(tabela.head())

tabcsv = pd.read_csv("C:/Users/Natanael V. de Sousa/OneDrive/Área de Trabalho/Programas/Análise de Dados/Arquivo_csv/species.csv")
print(tabcsv.shape)
print(tabcsv.head())
print(tabcsv.describe())

unidm = pd.Series(["Almofada","Colcholnet","End_ip","End_Mac"])
print(unidm)
from random import randint
numero = randint
lista = []
arrayl = np.array([(2,3,6,5),
                   (8,6,5,4),
                   (6,9,1,2)])
print(arrayl)

import sklearn.ensemble 