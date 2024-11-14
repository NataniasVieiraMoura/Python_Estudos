'''Suavização de imagems'''
import cv2 as cv

imagem = cv.imread("archive/data/lena.jpg")

#Dimensão para suavização
corpo = (5,5)

#Aplica o filtro de suavização blur
img_suave = cv.blur(imagem, corpo)#a imagem fica granulada

cv.imshow("Imagem original", imagem)
cv.imshow("Imagem suavizada", img_suave)
cv.waitKey(0)#Deve ser colocada para cancelar o contador de tempo de aba aberta
cv.destroyAllWindows()#Fecha todas as abas abertas