'''Redimensionamento de image para 200x200px:'''
import cv2
import numpy as np
import matplotlib as plt
import cv2 as cv

#Carregar imagem
carregar = cv.imread("archive/data/lena.jpg")

#Novas dimensões aplicadas a imagem
novas_dimensões = (200,200)

#Nova imagem com as novas dimesões aplicadas
#O método INTER_AREA é preferido para reduzir o tamanho de uma
#imagem. Ele funciona utilizando a relação da área dos pixels,geralmente
#resulta em uma imagem de melhor qualidade quando a imagem é reduzida.
imagem_redimensionada = cv.resize(carregar,novas_dimensões,interpolation=cv.INTER_AREA)

cv.imshow("Tamanho original",carregar)
cv.imshow("Transoformada",imagem_redimensionada)
cv.waitKey(0)
cv.destroyAllWindows()

print(f"\33[32mJustificativa:\nTratar imagems reduzidoas com o método interpolation=cv.INTER_AREA\n"
      f"faz com que a imagem fique mais rica em detanhes, transições de tons mais bem definidos\n"
      f"melhoram a precisão de algoritmos de IA ou de tratamento em geral. Perceba que o redimensionameto\n"
      f"beneficiou a qualidade da imagem visivelmente.\033[m")

