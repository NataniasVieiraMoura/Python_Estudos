import matplotlib.pyplot as plt#biblioteca de gráficos
from skimage.io import imread#biblioteca para adicionar imagems as tabelas
from matplotlib import figure#método que define dimensões para as tabelas
#linha 56: variavel recebe imagem pelo localização no diretorio com função imread("")
#endereço = imread("C:/Users/Natanael V. de Sousa/OneDrive/Imagens/imagems_piton/")
endereço = "C:/Users/Natanael V. de Sousa/OneDrive/Imagens/imagems_piton/"
lista = []
#plt.imshow(endereço)#para não ver uma por uma use um laço e veja todas
for i in range(0,9):
    imagem = imread(endereço+"imagem"+str(i+1)+".jfif")#variavel recebe as imagems
    lista.append(imagem)#adiciona as imagems
tamanho = plt.figure(figsize=(15,8))#define o tamanho dos gráficos
for i in range(0,9):#quantidade de elementos na lista que serão exibidos
    tamanho.add_subplot(3,3,i+1)#dimensões dos gráficos, no caso um 9x9(3 linhas e 3 colunas
    plt.imshow(lista[i])
plt.show()