import matplotlib.pyplot as plt, numpy as np

array = np.arange(-1000,1000,1)
calculo1 = array**2
calculo2 = array**3
calculo3 = -array**2
calculo4 = -array**3

#Resolvendo o problema do tamanho do gráfico:
'''Perceba que colocar esse subgráficos fica pequeno na tela.'''
'''Para resolver: use o método figure(figsize(linhas,colunas)) => com ele
    você pode alterar o tamanho da figura que será exibida'''
from matplotlib import figure
figura = plt.figure(figsize=(10,10))#altera as dimensões do gráfico
packcalculos = [calculo1,calculo2,calculo3,calculo4]
for i in range(0,4):#esse laço serve para ver todas as tabelas de uma unica vez
    figura.add_subplot(2,2,i+1)#esse i+1 é para que o quadrande não comece no 0(quadrante 0 não existe)
    #O método add_subplot() adiciona outros gráficos na tabela
    plt.plot(array,packcalculos[i])
plt.show()

