'''Subplots: Criando vários gráficos ao mesmo tempo com Matplotlib'''
'''Como criar vários gráficos ao mesmo tempo.'''
import matplotlib.pyplot as plt,numpy as np

array = np.arange(-1000,1000,1)
calculo = array**2
plt.plot(array,calculo)
plt.show()

calculo1 = array**2
calculo2 = array**3
calculo3 = -array**2
calculo4 = -array**3
'''O método subplot serve para quebrar o primeiro gráfico em seções:
    subplot tem os parametros: 
        em quantas linhas quer dividir,
        em quantas colunas quer dividir,
        qual o quadrante que a subplot vai aparecer'''
plt.subplot(2,2,1)#esse ultimo parametro mostra a seção que o subplot vai aparece
plt.plot(array,calculo1)#esse é o gráfico que o subplot se refere
plt.subplot(2,2,2)#segundo quadrante
plt.plot(array, calculo2)
plt.subplot(2,2,3)
plt.plot(array,calculo3)
plt.subplot(2,2,4)
plt.plot(array,calculo4)
#plt.show()

'''Abaixo, o segundo parametro define o gráfico em duas colunas'''
plt.subplot(1,2,1)#o ultimo parametro indica o primeiro quadrante
plt.plot(array, calculo2)#Essa linha define os dados para o subplot da linha 30
plt.subplot(1,2,2)#o ultimo paramentro indica o segundo quadrante
plt.plot(array,calculo4)
#plt.show()

'''Abaixo, o primeiro quadrado divide o gráfico em duas linhas'''
plt.subplot(2,1,1)
plt.plot(array,calculo1)
plt.subplot(2,1,2)
plt.plot(array,calculo3)
#plt.show()
