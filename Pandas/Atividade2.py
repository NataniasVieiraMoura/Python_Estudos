'''Conversão de imagem para a escala de cinza'''
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#Carregar imagem
imagem_original = cv.imread("archive/data/lena.jpg")

#Transforma em cinza para tratamento por IA
imagem_cinza = cv.cvtColor(imagem_original, cv.COLOR_RGB2GRAY)

#Criar subplots com parametros: numero de colunas, linhas e tamanho da imagem
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

#Exibir a primeira imagem no primeiro subplot
axs[0].imshow(imagem_original)#Imagem que aparecerá no fundo do gráfico
axs[0].set_title('Imagem Original')#Titulo do Subgráfico
axs[0].axis('off')# Desativar os eixos

#Exibir a segunda imagem no segundo subplot
axs[1].imshow(imagem_cinza)#Imagem que aparecerá no fundo do gráfico
axs[1].set_title('Imagem Trasformada')#Título do subgráfico
axs[1].axis('off')# Desativar os eixos

#Mostrar as imagens
plt.show()
print(f"\33[32mJustificativa:\nEm visão computacional, tranformar a escala em cinza"
      f"traz beneficios para o tratamento da imagem \npor um algoritmo que receberá um "
      f"escopo limitado de possíbilidades para análise, tornando seu \nprocessamento mais"
      f"preciso. Muitas cores sobrecarregariam um algoritmo que processa dados binárizados\033[m")