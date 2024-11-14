'''1ª Questão : Carregamento de imagems com o opencv'''

import cv2 as cv
import numpy as np
import matplotlib as plt

#Carregar imagem e função de classificador em cascata .xml
face_classifier = cv.CascadeClassifier("classificador.xml")
carregar = cv.imread("archive/data/lena.jpg")

#Transforma em cinza para tratamento por IA
imagem_gray = cv.cvtColor(carregar, cv.COLOR_RGB2GRAY)

#variavel recebe classificador em cascata com parametros:
#escala de processamento detecção em porcentagem e
#quantos vizinhos cada retângulo candidato deve ter para ser retido.
#Valores maiores resultam em menos detecções, mas com maior qualidade
faces = face_classifier.detectMultiScale(imagem_gray, 1.3,5)

#Abaixo um laço que vai cercar o perimetro do rosto encontrado
#Cria um retangulo ao redor do rosto encontrado com uma formúla para gráficos
for (x,y,w,h) in faces:
    #Cria um retangulo ao redor do ponto detectado como rosto
    #Define a borda com azul
    #Define a espessura da borda para 2
    cv.rectangle(carregar,(x,y),(x+w,y+h),(225,0,0),2)

#Abaixo retorna o grafico com a imagem de fundo tratada
cv.imshow("Lena-Imagem",carregar)#Nome do grafico seguido da imagem
cv.waitKey(0)#Define tempo que o gráfico ficará aberto quando executado
#cv.waitKey(10000)#Veja que aqui ele fecha depois de algums segundos
cv.destroyAllWindows()#Fecha todos os gráficos executados.

