import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("WIN_20240930_17_54_51_Pro.jpg")
imgc = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
#Divide o gráfico em dois para que cada um fique com uma imagem
#numero de linhas e colunas e a dimensão da imagem
axs[0].imshow(img)
#imagem que vai aparecer no primeiro gráfico
axs[0].set_title('Antes')
#nome do gráfico
axs[0].axis('off')
axs[1].imshow(imgc)
#imagem que vai aparecer no segundo gráfico
axs[1].set_title('Nova imagem')
#nome do segundo gráfico
axs[1].axis('off')
plt.show()
#mosta os gráficos
'''resposta: converter as imagem para cinza para que o algoritmo consiga interpletar
 por que uma ia so trata dados em base 2'''
